# -*- coding: utf-8 -*-

import html2text
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
if __name__ == '__main__':
    extractor_python_html.extract()