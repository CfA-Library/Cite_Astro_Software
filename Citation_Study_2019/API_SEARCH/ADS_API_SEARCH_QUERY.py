import requests
import json
import csv
import time
import codecs
import urllib
import cStringIO
from datetime import datetime
import requests.packages.urllib3
import re

requests.packages.urllib3.disable_warnings()

pubdate = "1997-01 TO 2018-04"

devkey = (open('dev_key.txt','r')).read()
keywords_list = (open('API_ALIAS_LIST.txt','r')).read()

keywords_list = keywords_list.splitlines()

class UnicodeWriter:
    def __init__(self, f, dialect=csv.excel, encoding="utf-8-sig", **kwds):
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()
    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        data = self.encoder.encode(data)
        self.stream.write(data)
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

url = 'https://api.adsabs.harvard.edu/v1/search/query/?q='


def getloopkeyword(body,daterange,devkey):
    query = 'body:%22'+ urllib.quote_plus(body) + '%22%20pubdate:%5B' + daterange + '%5D'    
    url_query = url + query
    headers = {'Authorization': 'Bearer '+devkey}
    content = requests.get(url_query, headers=headers)
    results = content.json()
    num = results['response']['numFound']
    return num
    

def keywordquery(body,daterange,devkey):

    rows = 100

    total = getloopkeyword(body,pubdate,devkey)
    loop = total/rows
    print("Looping script "+str(loop+1)+" times.")
    startnum = 0
    for i in range (0,loop+1):
        url1 = "https://ui.adsabs.harvard.edu/v1/search/query?q="
        query = 'body:%22'+ urllib.quote_plus(body) + '%22%20pubdate:%5B' + daterange + '%5D' + '&hl=true&indent=true&hl.snippets=4&hl.fragsize=99&hl.maxAnalyzedChars=550000&hl.fl=title,abstract,full,body,ack,doi,bibcode&fl=id,bibcode,alternate_bibcode,bibgroup,pub,identifier,doi,year,pubdate,ack,first_author,title&rows='+str(rows)+'&start='+str(startnum)
        url_query = url1 + query

        print(url_query)
        headers = {'Authorization': 'Bearer '+devkey}
        content = requests.get(url_query, headers=headers)
        results = content.json()

        hlights = results['highlighting']

        hldict = {}
        xlist = []
        
        for x in hlights:

            xlist.append(x)

            
        for i in xlist:
            print(i)
            try:
                context = hlights[i]['body']

                hldict[i] = context

            except KeyError:
                hldict[i] = ""

        docs = results['response']['docs']
        print(results)
        print(len(docs))

        for x in docs:

            bibcode = x['bibcode']
            year = x['year']
            pubdate2 = x['pubdate']

            try:
                docid = x['id']
                highlight = hldict[docid]
                string1 = ''.join(highlight)
                highlightclean = ' '.join(string1.split())
            except KeyError:
                docid = "broken"
                highlightclean = "none"
                print('no highlights')
            
            try:
                alternate_bibcode = x['alternate_bibcode']
                alternate_bibcode_clean = (('|').join(alternate_bibcode))
            except KeyError:
                alternate_bibcode_clean = ''

            try:
                identifier = x['identifier']
                identifier_clean = (('|').join(identifier))
            except KeyError:
                identifier_clean = ''

            try:
                doi = x['doi']
                doiclean = (('|').join(doi))
            except KeyError:
                doiclean = ''

            try:
                title = x['title']
                titleclean = (('|').join(title))
            except KeyError:
                titleclean = ''

            try:
                first_author = x['first_author']
            except KeyError:
                first_author = ''
          
            try:
                bibgroup = x['bibgroup']
                bibgroupclean = (('|').join(bibgroup))
            except KeyError:
                bibgroupclean = ''

            try:
                pub = x['pub']
            except KeyError:
                pub = ''


            row = [body]+[highlightclean]+[bibcode]+[alternate_bibcode_clean]+[bibgroupclean]+[pub]+[identifier_clean]+[doiclean]+[year]+[pubdate2]+[first_author]+[titleclean]
            wr.writerow(row)

        startnum += rows

        time.sleep(.5)


timestamp = datetime.now().strftime("%Y_%m%d_%H%M")

resultFile = open(pubdate+"_"+timestamp+".csv",'wb')
wr = UnicodeWriter(resultFile,dialect='excel',quoting=csv.QUOTE_ALL)

wr.writerow(['Alias']+['Highlight']+['Bibcode']+['Alternate_Bibcode']+['BibGroup']+['Publisher']+['Article_ID']+['DOI']+['Pub_Year']+['Pub_Date']+['Author']+['Title'])

bib_list = []

for x in keywords_list:
    keywordquery(x,pubdate,devkey)

resultFile.close()
