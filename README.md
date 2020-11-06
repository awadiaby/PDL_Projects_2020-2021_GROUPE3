# Wikitable Python Extactor

Our extractor written in python, extracts relevant tables from wikipedia links via HTML format and provides rendering in CSV format.
Then we compare the performance of our new extractor with those of an old version written in java which extracts via html and wikitext.

###########################################################################################################################################

>__PREREQUISITIES__

> PYTHON 

You need to install python on your computer:

          >WITH LINUX (UBUNTU)
          
                -$ sudo apt-get update
                -$ sudo apt-get install python3.9
                
          >WITH WINDOWS

              - Choose and download the lastest version of python (executable installer) on the following link https://www.python.org/downloads/windows/
              - Run Executable Installer and follow instructions
  
> clone and open the project (install git if you don't have it on your computer)

    - On your terminal use the following command to clone the project: git clone https://github.com/awadiaby/PDL_Projects_2020-2021_GROUPE3.git
    - Use the python editor of your choice to open the project (PyCharm, Spyder,vsCode...)

> Create directories trees on the project folder to store the extraction result

      >WITH LINUX
      
         - mkdir ./output/csv/
         - mkdir ./output/html

     >WITH WINDOWS

         - md ./output/csv/
         - md ./output/html

##############################################################################################################################################

>__REQUIREMENTS BEFORE RUNNING THE EXTRACTION__

Install python librairies required by the extractor

    >WITH LINUX
    
        - Library Requests: >$ pip install requests
        - Library Html2Text : >$ pip install html2text
        - Library beautifulsoup4 : >$ pip install beautifulsoup4

    >WITH WINDOWS
    
        - Library Requests: > py -m pip install requests
        - Library Html2Text : > py -m pip install html2text
        - Library beautifulsoup4 : > py- m pip install beautifulsoup4


##################################################################################################################################################

>__Run The project to extract__

To run the project you must excecute :

      >WITH LINUX
      
            $ python3 main.py

      >WITH WINDOWS
      
           py main.py

####################################################################################################################################################
> __Run test__

  To run the test:
  
    >WITH LINUX
      
            $ python3 unittest test_extractor

      >WITH WINDOWS
      
           py -m unittest test_extractor

###################################################################################################################################################

>__Improvements__

>- Log 404 error urls in some file for analysis
>- Consider colspan.s as one csv column
>- More tests on functions

###################################################################################################################################################

Authors: 

  > Diaby Awa
  > Thibaut Assogba
  > Safietou Diallo
  > MAurice AKA
  
Copyright:2020

__Happy Coding !__
