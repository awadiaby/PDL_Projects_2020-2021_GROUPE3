# -*- coding: utf-8 -*-

import os
import unittest
import requests
from csv_diff import load_csv, compare

from Extractor_python_html import Extractor_python_html


class TestExtractor(unittest.TestCase):
    
    def save_table_to_csv(self, wikiurl, outputFolderName):
        extractor_python_html = Extractor_python_html()
        #wikiurl = wikiurl[0:-1]
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
                    extractor_python_html.output_csv_file2(name="{}_{}".format(wikiurl, i), content=wikicsv, outputFolderName=outputFolderName) #save it to file
                except Exception as e:
                    print("Smthg went wrong on table : {} \nError : {}".format(i, e))

    
    
    
    #this function tests the number of valid url or not and the total number of url in the wikiurls table 
    def test_url_file(self):
        extractor_python_html = Extractor_python_html()
        BASE_WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/"
        wikiurls = extractor_python_html.load_file_content('wikiurls.txt')
        nbUrlOk = 0
        nb_urls_no_ok= 0
        for wikiurl in wikiurls:
            wikiurl = wikiurl[0:-1] # To delete the \n at the end of the url
            url = "{}{}".format(BASE_WIKIPEDIA_URL, wikiurl) # build real URL
                
            try:
                response = requests.get(url)
                response.raise_for_status()
                if response.status_code == 200:
                    nbUrlOk += 1
            except requests.exceptions.HTTPError as errh:
                if(errh.response.status_code == 404):
                    nb_urls_no_ok += 1
                print ("Http error : ",errh)
            except requests.exceptions.ConnectionError as errc:
                print ("Error connecting : ",errc)
            except requests.exceptions.Timeout as errt:
                print ("Timeout error : ",errt)
            except requests.exceptions.RequestException as err:
                print ("Oops ! Something wrong : ",err)
      
        print("*****end  : url_ok= ",nbUrlOk)
        self.assertEqual(nbUrlOk, 304)
        self.assertEqual(nb_urls_no_ok, 32)
        self.assertEqual(len(wikiurls), 336)
        
    #test if the size of a file is greater than 0
    def is_non_zero_file(self, fpath):  
        return os.path.isfile(fpath) and os.path.getsize(fpath) > 0
    
    #test if all csv files containt datas    
    def test_performance_extractor1(self):  
        
        folder_path = "C:/Users/safie/Desktop/PDL_WikiExtractor/PDL_Projects_2020-2021_GROUPE3/output/csv"
        nbOfEmptyFiles = 0
        for path, dirs, files in os.walk(folder_path):
            for filename in files:
                filepath = folder_path + '/' + filename.rstrip("\n")
                if not self.is_non_zero_file(filepath) :
                    nbOfEmptyFiles += 1
        
        self.assertEqual(nbOfEmptyFiles, 0)
        
        
        
    def test_extract_wikitables_1(self):
        extractor_python_html = Extractor_python_html()
        result, nbwikitables = extractor_python_html.extract_wikitables(wikiurl='Comparison_of_email_clients')
        self.assertTrue(result)
        self.assertEqual(nbwikitables, 11)

    def test_extract_wikitables_2(self):
        extractor_python_html = Extractor_python_html()
        result, nbwikitables =  extractor_python_html.extract_wikitables(wikiurl='Comparison_of_HTML_editors')
        self.assertTrue(result)
        self.assertEqual(nbwikitables, 7)
  
  
    
    def test_extractor(self):
        
        extractor_python_html = Extractor_python_html()
        extract_done = False
        extractor_python_html.extract()
        extract_done = True
        self.assertTrue(extract_done, "Extraction failed")

            
    # Extracting the tables of an url several times and check if the results are the same
    def test_performance_extractor2(self):
        truth_tables_folder_path = "C:/Users/safie/Desktop/PDL_WikiExtractor/PDL_Projects_2020-2021_GROUPE3/output/truth_tables"
        test_tables_folder_path = "C:/Users/safie/Desktop/PDL_WikiExtractor/PDL_Projects_2020-2021_GROUPE3/output/test_tables"
        nb_of_differences = 0
        url = "Comparison_between_Esperanto_and_Ido"
        # saving the first extraction tables in "truth_tables"
        self.save_table_to_csv(url, 'truth_tables')
        list_of_truth_tables = os.listdir(truth_tables_folder_path)
        
        for i in  range(10):
            self.save_table_to_csv(url, 'test_tables')
            # reading tables from csv files
            list_of_test_tables = os.listdir(test_tables_folder_path)
            
            for i in range(len(list_of_truth_tables)):
                truth_table_file_name = list_of_truth_tables[i]
                test_table_file_name = ""
                if truth_table_file_name in list_of_test_tables:
                    test_table_file_name = truth_table_file_name
                if not test_table_file_name.strip():
                    test_table_filepath = test_tables_folder_path + '/' + test_table_file_name.rstrip("\n")
                    truth_table_file_path = truth_tables_folder_path + '/' + truth_table_file_name.rstrip("\n")
                    # compare csv files
                    diff = compare(load_csv(open(test_table_filepath)), load_csv(open(truth_table_file_path)))
                    if not diff.strip():
                        nb_of_differences += 1
                        print("nb_of_differences : ", nb_of_differences)
        self.assertEqual(nb_of_differences, 0)
        
             
if __name__ == '__main__':
        unittest.main()  