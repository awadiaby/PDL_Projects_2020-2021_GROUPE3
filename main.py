# install some libs
#!pip install requests
#!pip install html2text

#####################
# imports
#####################
import requests
import html2text
from bs4 import BeautifulSoup

#####################
# global variables
#####################
BASE_WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/"
h2txt = html2text.HTML2Text()

#####################
# Functions
#####################

# Load input file to array
def load_file_content(file):
    with open("inputdata/{}".format(file), 'r') as f:
        data = f.readlines()

    return data


# Return html content from url and None if smthg wrong happened
def read_url_html_content(url):

    url = "{}{}".format(BASE_WIKIPEDIA_URL, url) # build real URL

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as errh:
        print ("Http error : ",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error connecting : ",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout error : ",errt)
    except requests.exceptions.RequestException as err:
        print ("Oops ! Something wrong : ",err)

    return None


# Read HTML content and capture all <table> tags in some array
def get_tables_from_html(html_content):
    
    soup = BeautifulSoup(html_content, "html.parser")
    wikitables = soup.find_all('table', class_ = 'wikitable') # get all table tag with wikitable class
    
    #wikitables = [table for table in tables if table.get('class') is not None and ("wikitable" in table.get('class'))]
    return wikitables


# Clean a given table cell (td or th) content from html to text
def get_cleaned_table_cell(html_cell):
    temp_txt = h2txt.handle(str(html_cell)) # make sure it a str param
    soup = BeautifulSoup(temp_txt, 'html.parser')
    cleaned_content = soup.get_text().replace("\n", "")
    return cleaned_content


# input data : table_tag <table>........</table>
# return : equivalent table as csv
def read_table_tag_to_csv(wikitable):

    csv = ''
    soup = BeautifulSoup(str(wikitable), "html.parser")

    lines = soup.tbody.find_all('tr')

    for line in lines:

        new_line = ''
        for child in line: # for each column (td, th, ...) tags
            
            cell_content = str(child).replace("\n", "")

            if cell_content and ("<" in cell_content): # cell not empty and is and HTML tag

                cleaned_content = get_cleaned_table_cell(str(child).replace("\n", ""))
                new_line += '"{}";'.format(cleaned_content)

        new_line = new_line[0:-1] # remove last ';' added
        csv += '{}\n'.format(new_line)

    csv = csv[0:-1] # remove last \n char added

    return csv


# Write csv content to csv directory with name
def output_csv_file(name, content):
    with open('output/csv/{}.csv'.format(name), 'w', encoding ='utf-8') as handler:
        handler.write(content)

# Write html content to html directory with name
def output_html_file(name, content):
    with open('output/html/{}.html'.format(name), 'w', encoding ='utf-8') as handler:
        handler.write(content)


def extract_wikitables(wikiurl):

    # read HTML content from url
    wiki_html_content = read_url_html_content(url=wikiurl)

    if wiki_html_content is not None: # everything went fine

        # save html file
        output_html_file(name=wikiurl, content=wiki_html_content)

        # get tables in html content
        wikitables = get_tables_from_html(wiki_html_content)

        i = 0
        for wikitable in wikitables:
                
            i += 1
            try:
                wikicsv = read_table_tag_to_csv(wikitable=wikitable)  #read table to csv
                output_csv_file(name="{}_{}".format(wikiurl, i), content=wikicsv) #save it to file
            except Exception as e:
                print("Something went wrong on table : {} \nError : {}".format(i, e))
                return False, 0
    else:
        return False, 0

    return True, i



def extract():
    # Load urls in variable
    wikiurls = load_file_content("wikiurls.txt")

    n = 0
    for wikiurl in wikiurls:
        n += 1
        print("Loading url {} ...".format(n))
        wikiurl = wikiurl[0:-1]
        extract_wikitables(wikiurl=wikiurl)

        




####################
# Main
####################
if __name__ == '__main__':
    extract()
    print("All done !")
