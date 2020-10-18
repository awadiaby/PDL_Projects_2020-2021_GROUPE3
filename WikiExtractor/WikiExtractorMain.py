# -*- coding: utf-8 -*-
"""
- une methode pour lire le fichier contenant les urls et stocke
ces derniers dans un tableau
- une fonction main() qui contient une boucle parcourant le tableau des urls précédent
et qui utilise la classe TablesExtractor pour faire les traitements
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
        #urls.append(WIKI_BASE_URL + shortUrl)
    urlsFile.close()
        





#======================== Main ====================

tablesExtractor = TablesExtractor()
read_urls_file()
output_folder = "output_folder"

print("***************** Begin Extract *****************")
for shortUrl, url in urls.items():
    print("url : ", url)
    tables = tablesExtractor.get_all_tables(url)
    #tableIdex = 0
    for tableIdex in range(len(tables)):
        output_fileName = shortUrl.rstrip("\n") + '-' + str(tableIdex) + '.csv'
        print("outputFileName : ",output_fileName)
        tablesExtractor.write_table_to_csv(tables[tableIdex], output_fileName, output_folder)
        
print("***************** Extract finished *****************")
