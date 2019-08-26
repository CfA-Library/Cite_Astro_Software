import os.path
import re
import csv
from io import open
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf8')

root_path = ''

searchstring = ''
p = re.compile(searchstring)

CSVFILENAME = ''

result = []


def find_tags(tag, depth):
    data = ["" for i in range(depth)]
    parent_number = 1
    while tag.parent and depth > 0:
        data[parent_number - 1] = [tag.parent.name, "".join([str(i) for i in tag.parent.contents])]
        if len(data[parent_number - 1][1]) > 10:
            data[parent_number - 1] = [tag.parent.name, data[parent_number - 1][1][:10000]]
        tag = tag.parent
        depth -= 1
        parent_number += 1
    return data


def find_alias(tag):
    text = "".join([str(i) for i in tag.parent.contents])
    alias = re.findall(p, text)
    hit = re.search(p, text)
    if hit:
        index = hit.regs[0]
        return alias, text[index[0]:index[1]]
    else:
        return alias, "No Alias"


def csv_saver(data, filename):
    path = filename + '.csv'
    print('Now saving as .CSV file:', path)
    with open(path, mode='wb') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data[0][0])
        for each in data:
            writer.writerow(each[1])
    print('CSV has been created.')


for directory_name, sub_directory, fileList in os.walk(root_path):
    print('Directory located: %s' % directory_name)

    for xml_file in fileList:
        if xml_file.endswith(".xml"):

            textfile = open(directory_name + '/' + xml_file, 'r', encoding='ISO-8859-1')
                #ISO-8859-1 encoding for some ApJ files
            contents = textfile.read()
            textfile.close()

            soup = BeautifulSoup(contents, "lxml")
            all = soup.findAll(text=p)
            for tag in all:
                alias_a, alias_b = find_alias(tag)
                tag_data = find_tags(tag, 4)
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

                result.append(
                    [['File_Name', 'Publication_Date', 'Title', 'Author(s)', 'Journal_Title', 'Publisher', 'Bibcode',
                      'Keyword', "alias_unique", "Parent1_Tag", "Parent1_Content", "Parent2_Tag",
                      "Parent2_Content", "Parent3_Tag", "Parent3_Content", "Parent4_Tag"],
                     [xml_file, date.year.text, titles_clean, authors_clean, journal.text,
                      publisher.text, bibcode_clean, alias_b, alias_a, tag_data[0][0], [tag_data[0][1]], tag_data[1][0],
                      [tag_data[1][1]], tag_data[2][0], [tag_data[2][1]], tag_data[3][0] ]])

else:
    print('This file is not XML.')

print('All XML files in directory have been parsed.')
if result:
    csv_saver(result, CSVFILENAME)