# -*- coding: utf-8 -*-

import requests
import html2text
from bs4 import BeautifulSoup
import Extractor_python_html
from Extractor_python_html import Extractor_python_html

#####################
# global variables
#####################

BASE_WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/"
h2txt = html2text.HTML2Text()


##################################
#
# MAIN
#
##################################
# Load urls in variable
extractor_python_html = Extractor_python_html()
wikiurls=extractor_python_html.load_file_content("wikiurls.txt")


n = 0

for wikiurl in wikiurls:

    n += 1
    #print("Loading url {} ...".format(n))

    wikiurl = wikiurl[0:-1]
    # read HTML content from url
    wiki_html_content = extractor_python_html.read_url_html_content(url=wikiurl)
    

    if wiki_html_content is not None: # everything went fine

        # save html file
        extractor_python_html.output_html_file(name=wikiurl, content=wiki_html_content)

        # get tables in html content
        wikitables = extractor_python_html.get_tables_from_html(wiki_html_content)

        i = 0
        for wikitable in wikitables:
            
            i += 1
            try:
                wikicsv = extractor_python_html.read_table_tag_to_csv(wikitable=wikitable)  #read table to csv
                extractor_python_html.output_csv_file(name="{}_{}".format(wikiurl, i), content=wikicsv) #save it to file
            except Exception as e:
                print("Smthg went wrong on table : {} \nError : {}".format(i, e))


print("All done !")