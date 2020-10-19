# -*- coding: utf-8 -*-

# HTML parsing
import os
from bs4 import BeautifulSoup as soup
# Web client
from urllib.request import urlopen as uReq
import urllib.request
""" """
class TablesExtractor:

    
    """ An wikipedia table extractor"""
    """
    - Avoir un attribut pour l'url
    - Avoir une methode pour requeter l'url
    - Une methode isReleventTable(table)
    - methode is_url_ok(url)
    - methode get_all_tables
    - methode pour ecrire une table dans un csv write_table_to_csv()
    """ 
    #this method check if the url is ok
    def is_ok_url(self, url):
        request = urllib.request.Request(url)
        request.get_method = lambda: 'HEAD'
        try:
            urllib.request.urlopen(request)
            return True
        except  urllib.request.HTTPError:
            return False
   
    """Function extracting all tables from a given webpage, parameter = URL string"""
    def get_all_tables(self, url):
       if self.is_ok_url(url):
            uClient = uReq(url)
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, "html.parser")
            tables = page_soup.find_all("table")
           # print(tables[0])
            return tables
       return []
     
        
    #this method check if the tables is relevant
    def is_relevent(self, table):
        th_set = table.find_all("tr")
        print("*********** table relevent" ,th_set)
        if len(th_set)<=2:
            return False
        elif len(th_set)>2:
            return True
    """
    table : 
    outputfolder : 
    """
    def write_table_to_csv(self, table, output_fileName, output_folder, delimiter=";"):
       if not os.path.exists(output_folder):
            os.mkdir(output_folder)
       with open(output_folder+"/"+output_fileName, "w", encoding="utf-8") as output_file:
        # Table header from <th> cells
        header = ""
        th_set = table.find_all("th")
        for i in range(len(th_set)):
            th_data = th_set[i].text.rstrip('\n')
            if i == len(th_set) - 1:
                header += f"{th_data}\n"
            else:
                header += f"{th_data}{delimiter}"
        #if self.is_relevent(table):
        output_file.write(header)
        # Table data from <td> cells for each <tr> row
        tr_set = table.find_all("tr")
        for tr in tr_set:
            line = ""
            td_set = tr.find_all("td")
            for i in range(len(td_set)):
                td_data = td_set[i].text.rstrip('\n')
                if i == len(td_set) - 1:
                    line += f"{td_data}\n"
                else:
                    line += f"{td_data}{delimiter}"
        #if self.is_relevent(table):
        output_file.write(line)
            