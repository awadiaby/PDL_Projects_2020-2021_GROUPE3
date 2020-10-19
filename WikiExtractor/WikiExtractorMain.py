# -*- coding: utf-8 -*-
"""

"""
from TablesExtractor import TablesExtractor
import os

#output_folder=os.mkdir('C:\\Users\\safie\\Desktop\\PDL_WikiExtractor\\WikiExtractor\\output_folder')
WIKI_BASE_URL = "https://en.wikipedia.org/wiki/"
urls = {}

def read_urls_file():
    urlFilePath = './input_data/wikiUrls.txt'
    if not os.path.exists(urlFilePath):
        print("The urls file does'nt exists !!!")
        exit(-1)
    urlsFile = open(urlFilePath, "r")
    for shortUrl in urlsFile.readlines():
        urls[shortUrl] = WIKI_BASE_URL + shortUrl
    urlsFile.close()
        

#======================== Main ====================

tablesExtractor = TablesExtractor()
read_urls_file()
output_folder = "output_folder"

print("***************** Begin Extract *****************")
for shortUrl, url in urls.items():
    print("url : ", url)
    tables = tablesExtractor.get_all_tables(url)
    for tableIdex in range(len(tables)):
        output_fileName = shortUrl.rstrip("\n") + '-' + str(tableIdex) + '.csv'
        print("outputFileName : ",output_fileName)
        if tablesExtractor.is_relevent(tables[tableIdex]):
           tablesExtractor.write_table_to_csv(tables[tableIdex], output_fileName, output_folder)
        
print("***************** Extract finished *****************")
