import os.path
import re
import csv
from bs4 import BeautifulSoup

rootDir = ''

searchstring = ''
patterns = re.compile(searchstring)

CSVFILENAME = ''

result = []


def find_tags(tag, deepth):
    data = ["" for i in range(deepth)]
    parent_num = 1
    while tag.parent and deepth > 0:
        data[parent_num - 1] = [tag.parent.name, "".join([str(i) for i in tag.parent.contents])]
        if len(data[parent_num - 1][1]) > 10:
            data[parent_num - 1] = [tag.parent.name, data[parent_num - 1][1][:10000]]
        tag = tag.parent
        deepth -= 1
        parent_num += 1
    print(data)
    return data


def merge(data, index):
    if index < len(data):
        if type(data[index]) == str:
            d = merge(data, index + 1)
            if data[index] and d:
                return data[index] + " ; " + d
            elif d:
                return d
            else:
                return data[index]
        else:
            d = merge(data[index], 0)
            dd = merge(data, index + 1)
            if d and dd:
                return d + " ; " + dd
            elif d:
                return d
            elif dd:
                return dd
            else:
                return ""
    else:
        return ""


def find_alias(tag):
    text = "".join([str(i) for i in tag.parent.contents])
    alias = merge(re.findall(patterns, text), 0)
    hit = re.search(patterns, text)
    if hit:
        index = hit.regs[0]
        return alias, text[index[0]:index[1]]
    else:
        return alias, "No Alias"


def csv_saver(data, filename):
    path = filename + '.csv'
    print('Now saving as .CSV file:', path)
    with open(path, mode='w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data[0][0])
        for each in data:
            writer.writerow(each[1])
    print('CSV has been created.')


for dirName, subdirList, fileList in os.walk(rootDir):
    print('Directory located: %s' % dirName)

    for xmlfile in fileList:
        if xmlfile.endswith(".xml"):

            textfile = open(dirName + '/' + xmlfile, 'r', encoding='ISO-8859-1')
                #ISO-8859-1 encoding for some ApJ files
            contents = textfile.read()
            textfile.close()

            soup = BeautifulSoup(contents, "lxml")
            all = soup.findAll(text=patterns)
            for tag in all:
                malias, mkeyword = find_alias(tag)
                t_data = find_tags(tag, 4)
                date = soup.article.find("pub-date")
                titles = soup.article.find_all("article-title")
                authors = soup.article.find_all("name")
                journal = soup.article.find("journal-title")
                publisher = soup.article.find("publisher-name")
                
                bibcode = soup.article.find_all("article-id")
                bibcode_clean = ", ".join([bibcode.text for bibcode in bibcode])
                
                titles_clean = [title.text for title in titles]
                titles_clean = ", ".join(titles_clean)
                try:
                    titles_clean.index("High&hyphen;")
                    titles_clean = titles_clean[12:]
                except:
                    pass

                authors_clean = [name.text for name in authors]
                authors_clean = " ".join("".join(authors_clean).split("\n"))

                print('File_Name:', xmlfile)
                print('Keyword:', mkeyword)

                result.append(
                    [['File_Name', 'Publication_Date', 'Title', 'Author(s)', 'Journal_Title', 'Publisher', 'Bibcode',
                      'Keyword', "alias_unique", "Parent1_Tag", "Parent1_Content", "Parent2_Tag",
                      "Parent2_Content", "Parent3_Tag", "Parent3_Content", "Parent4_Tag", "Parent4_Content"],
                     [xmlfile, date.year.text, titles_clean, authors_clean, journal.text,
                      publisher.text, bibcode_clean, mkeyword, malias, t_data[0][0], [t_data[0][1]], t_data[1][0],
                      [t_data[1][1]], t_data[2][0], [t_data[2][1]], t_data[3][0], [t_data[3][1]]  ]])

else:
    print('This file is not XML.')

print('All XML files in directory have been parsed.')
if result:
    csv_saver(result, CSVFILENAME)
