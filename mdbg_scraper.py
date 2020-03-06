#this program gets HTML from MDBG for a given character, lints it, and makes a list of the phrases containing the character
import requests
import subprocess as sproc
import os

XSL = "./mdbg_entry_to_list.xsl"

def get_mdbg_list(ch, unprocessed_list):
    search_url = f'https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb=c%3A*{ch}*'
    unlinted_file = f"./tmp/unlinted_{ch}.html"
    linted_file = f"./tmp/linted_{ch}.xml"
    
    #make empty files first so the shell commands don't freak
    open(unlinted_file, 'a').close()
    open(linted_file, 'a').close()

    #write the raw html to 'unlinted_file'
    raw_html = requests.get(search_url).content
    with open(unlinted_file, 'w') as file:
        file.write(raw_html.decode('UTF-8'))

    #lint the file
    lint_cmd = f"xmllint -html -xmlout -o {linted_file} {unlinted_file} > /dev/null 2>&1"
    p = sproc.Popen(lint_cmd, shell=True)
    p.communicate()

    #transform the file
    #-o output path
    #-s input path
    #-xsl path to xsl
    saxon_cmd = f"saxonb-xslt -o {unprocessed_list} -s {linted_file} -xsl {XSL}"
    p = sproc.Popen(saxon_cmd, stdout=sproc.PIPE, shell=True)
    p.communicate()

    os.remove(unlinted_file)
    os.remove(linted_file)

    print(f"List of phrases containing {ch} scraped from MDBG and saved to {unprocessed_list}")
