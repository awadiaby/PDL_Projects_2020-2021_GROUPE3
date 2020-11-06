call echo "EXECUTION DU SCRAPER JAVA"
call echo "install dependencies"
call mvn compile -f "D:\Awa\PDL\PDL_1920_groupe-7"
call echo "compiler et executer un java"
call mvn package -f "D:\Awa\PDL\PDL_1920_groupe-7" 
cd "D:\Awa\PDL/PDL_1920_groupe-7"
call echo "-------------------------------------------------------"
call java -cp "./target\WikipediaMatrix-1.0-Release.jar" fr.istic.pdl1819_grp5.wikiMainwikitext

call java -cp "./target\WikipediaMatrix-1.0-Release.jar" fr.istic.pdl1819_grp5.wikiMainhtml

call echo "------- Temps exécution --------------------------"
cd ..
set /p timeWikitxt=<"PDL_1920_groupe-7\temps-execution-wikitext.txt"
echo " Temps Exécution %timeWikitxt% "
set /p timeHtml=<"PDL_1920_groupe-7\temps-execution-html.txt"
echo " Temps Exécution %timeHtml% "
call echo "--------------- Nombre de fichier --------------------------------"
set /p numberWikitxt=<"PDL_1920_groupe-7\numberFileWiki.txt"
echo " Nombre de Fichier wikitext %numberWikitxt% "
set /p numberHtml=<"PDL_1920_groupe-7\numberFilehtml.txt"
echo " Nombre de Fichier html %numberHtml% "



set nbLines=cat ".\PDL_1920_groupe-7\temps-execution-wikitext.txt"
call echo "EXECUTION DU SCRAPER PYTHON"
call echo "------------------------------------"
cd "D:\Awa\PDL/PDL_Projects_2020-2021_GROUPE3"
call python main.py"
call echo "----------------------------- temps exécution python---------------"
set /p timeHtmlPy=<"PDL_Projects_2020-2021_GROUPE3\temps-execution.txt"
call echo "----------------------------- nombre de fichiers python---------------"
set /p numberHtmlPy=<"PDL_Projects_2020-2021_GROUPE3\number-execution.txt"

if %numberHtml% LSS %numberHtmlPy% echo "le nombre de fichier java est plus petit que celui de python"
if %numberHtml% GTR  %numberHtmlPy% echo "le nombre de fichier java est plus grand que celui de python"

if %timeHtml% LSS %timeHtmlPy% echo "le temps d'exécution du SCRAPER java est plus petit que celui de python"
if %timeHtml% GTR %timeHtmlPy% echo "le temps d'exécution du SCRAPER java est plus grand que celui de python"




