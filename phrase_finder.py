#comma separated list of known characters
  #can get all hsk 2 chars, and add hsk 3 chars that I've already done
    #xsl for this already?
#list of possible phrases per character
  #
#filter on phrases for which all containing characters are in list

import argparse
import os
from datetime import date
from mdbg_scraper import get_mdbg_list
import anki_searcher as anki

parser = argparse.ArgumentParser(description='For one or more Chinese characters, get a list of words with characters, pinyin, and definitions')
parser.add_argument("-c", nargs=1, type=str, help="The character of interest.")
parser.add_argument("-n", action="store_true", help="Only keep new phrases.")

args = parser.parse_args()
ch = args.c[0]
new_only = args.n

processed_list = f"./tmp/processed_{ch}_list_{date.today()}"
unprocessed_list = f"./tmp/unprocessed_{ch}_list_{date.today()}"

def make_unprocessed_list(ch, unprocessed_list):
    get_mdbg_list(ch,unprocessed_list)

def chars_only(full_phrase):
    return full_phrase.split(" (")[0]

def composite_chars_known(phrase):
    chars = chars_only(phrase)
    return all(anki.character_exists(char) for char in chars)

def is_new(phrase):
    chars = chars_only(phrase)
    return not anki.phrase_exists(chars)

def choose_phrases():
    potential_phrases = get_unprocessed_list()

    final = list(filter(composite_chars_known, potential_phrases))
    if new_only:
        final = list(filter(is_new, final))

    return final

def get_unprocessed_list():
    with open(unprocessed_list, 'r') as phrase_file:
        return phrase_file.read().splitlines()

def write(final_list):
    with open(processed_list, 'w') as f:
        for entry in final_list:
            f.write(entry+'\n')

def delete_unprocessed_list():
    os.remove(unprocessed_list)
    print("Unprocessed list deleted")

#main
make_unprocessed_list(ch, unprocessed_list)
final_list = choose_phrases()
write(final_list)
delete_unprocessed_list()
print(f"List of {'new ' if new_only else ''}phrases with familiar characters created")
