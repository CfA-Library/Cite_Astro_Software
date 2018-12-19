import os.path
import re
import csv
from bs4 import BeautifulSoup

rootDir = '/Users/robin/desktop/TEST/'

searchstring = 'AstroPy|astroPy|astropy|NumFOCUS|MaLTPyNT|DS9\b|ds9\b|SAOImage|saoimage|SAOImageDS9|SAOtng|pyds9|TkSAO|Houdini|houdini|ytini\b|SideFX|AstroBlend|astroblend|Blender|PlasmaPy|plasmapy|NumPy|SciPy|Spec2d\b|spec2d\b|DEEP2|DEIMOS|WCS Tools|WCSTools|wcs tools|wcstools|imwcs|imcat\b|sky2xy|xy2sky|sethead|gethead|WCSLIB|LibWCS|RADMC-3D|radmc3dPy|RADMC3D|RADMC|radmc|radmc3d|TARDIS|TARDIS-SN|tardis|Tardis|Stingray|StingRay|stingray|2016ascl.soft08001H|BEANS|Beans|beans|Apache Hadoop|Apache Pig|MOCCA'
patterns = re.compile(searchstring)

CSVFILENAME = '/Users/robin/desktop/scripts/citationproject'

result = []


def get_tags(tag, deepth):
    data = ["" for i in range(deepth)]
    parent_num = 1
    while tag.parent and deepth > 0:
        data[parent_num - 1] = [tag.parent.name, "".join([str(i) for i in tag.parent.contents])]
        if len(data[parent_num - 1][1]) > 100:
            data[parent_num - 1] = [tag.parent.name, data[parent_num - 1][1][:50]]
        tag = tag.parent
        deepth -= 1
        parent_num += 1

    return data


def deepjoin(data, index):
    if index < len(data):
        if type(data[index]) == str:
            d = deepjoin(data, index + 1)
            if data[index] and d:
                return data[index] + " ; " + d
            elif d:
                return d
            else:
                return data[index]
        else:
            d = deepjoin(data[index], 0)
            dd = deepjoin(data, index + 1)
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


def get_keyword(tag):
    text = "".join([str(i) for i in tag.parent.contents])
    keywords = deepjoin(re.findall(patterns, text), 0)
    match = re.search(patterns, text)
    if match:
        index = match.regs[0]
        return keywords, text[index[0]:index[1]]
    else:
        return keywords, "n/a"


def save_to_csv(data, filename):
    path = filename + '.csv'
    print(' Saving to csv:', path)
    with open(path, mode='w', encoding='utf-8') as file:
        data_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(data[0][0])
        for each in data:
            data_writer.writerow(each[1])
    print('CSV saved. Done')


for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)

    for xmlfile in fileList:
        if xmlfile.endswith(".xml"):

            textfile = open(dirName + '/' + xmlfile, 'r', encoding='ISO-8859-1')
            contents = textfile.read()
            textfile.close()

            soup = BeautifulSoup(contents, "lxml")
            all = soup.findAll(text=patterns)
            for tag in all:
                mkeywords, mkeyword = get_keyword(tag)
                t_data = get_tags(tag, 2)
                date = soup.article.find("pub-date")
                titles = soup.article.find_all("article-title")
                authors = soup.article.find_all("name")
                journal = soup.article.find("journal-title")
                publisher = soup.article.find("publisher-name")
                bibcode = soup.article.find_all("article-id")

                all_titles = [title.text for title in titles]
                all_titles = ", ".join(all_titles)
                try:
                    all_titles.index("High&hyphen;")
                    all_titles = all_titles[12:]
                except:
                    pass
                all_authors = [name.text for name in authors]
                all_authors = " ".join("".join(all_authors).split("\n"))
                all_bibcode = ", ".join([bibcode.text for bibcode in bibcode])
                print('--File Name:', xmlfile)
                print('--Keyword:', mkeyword)
                print('--Paper pub-year:', date.year.text)
                print('--Title: ', all_titles)
                print('--Authors: ', all_authors)
                print('--Journal:   ', journal.text)
                print('--Publisher:   ', publisher.text)
                print('--Bibcode:   ', all_bibcode)

                result.append(
                    [['File_Name', 'Publication_Date', 'Title', 'Author(s)', 'Journal_Title', 'Publisher', 'Bibcode',
                      'Keyword', "Keywords_unique", "Parent1_Tag", "Parent1_Content", "Parent2_Tag",
                      "Parent2_Content", ],
                     [xmlfile, date.year.text, all_titles, all_authors, journal.text,
                      publisher.text, all_bibcode, mkeyword, mkeywords, t_data[0][0], t_data[0][1], t_data[1][0],
                      t_data[1][1]]])

else:
    print('File not xml')

print('DONE PROCESSING XML')
if result:
    save_to_csv(result, CSVFILENAME)