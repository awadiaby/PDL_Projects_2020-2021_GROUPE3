import os
import unittest
import requests
from os import path
from main import extract, extract_wikitables, extract_wikitables,output_csv_file,load_file_content,read_url_html_content

class TestExtractor(unittest.TestCase):

    # constants

    # check the existence of the outpout folders

    def test_check_output(self):
        self.assertTrue(path.exists("output/html"))
        self.assertTrue(path.exists("output/csv"))

    # check url numbers (valid and invalid) 

    def test_url_file(self):
        BASE_WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/"
        wikiurls = load_file_content("wikiurls.txt")
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

        self.assertEqual(nbUrlOk, 301)
        self.assertEqual(nb_urls_no_ok, 35)
        self.assertEqual(len(wikiurls), 336)


    def test_extractor(self):
        extract_done = False
        extract()
        extract_done = True
        self.assertTrue(extract_done, "Extraction failed")


    def test_extract_wikitables_1(self):
        result, nbwikitables = extract_wikitables(wikiurl='Comparison_of_email_clients')
        self.assertTrue(result)
        self.assertEqual(nbwikitables, 11)

    def test_extract_wikitables_2(self):
        result, nbwikitables = extract_wikitables(wikiurl='Comparison_of_HTML_editors')
        self.assertTrue(result)
        self.assertEqual(nbwikitables, 7)
  
    #test if the size of a file is greater than 0

    def is_non_zero_file(self, fpath):  
        return os.path.isfile(fpath) and os.path.getsize(fpath) > 0
    
    #test if all csv files containt datas    
    def test_performance_extractor1(self):  
        
        folder_path = "output/csv"
        nbOfEmptyFiles = 0
        for path, dirs, files in os.walk(folder_path):
            for filename in files:
                filepath = folder_path + '/' + filename.rstrip("\n")
                if not self.is_non_zero_file(filepath) :
                    nbOfEmptyFiles += 1
        
        self.assertEqual(nbOfEmptyFiles, 0)
         
            
    # Extracting the tables of an url several times and check if the results are the same
    def test_performance_extractor2(self):
        truth_tables_folder_path = "output/truth_tables"
        test_tables_folder_path = "output/test_tables"
        nb_of_differences = 0

        # saving the first extraction tables in "truth_tables"
        output_csv_file(url, 'output/truth_tables')
        self.extract_wikitables(wikiurl='Comparison_between_Esperanto_and_Ido')
        list_of_truth_tables = os.listdir(truth_tables_folder_path)
        
        for i in  range(10):
            output_csv_file(url, 'test_tables')
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
