#!/bin/bash

#1. pull in character
CHAR="$1"

#2. run the python script
python3 phrase_finder.py -c $CHAR -n

#3. pass the file contents to email
MY_EMAIL="someone@somewhere.com"
EXPERT_EMAIL="someone_else@somewhere.com"
SMTP=""
CC=""
PWD=""
DTE=$(date +%Y-%m-%d)
SUBJECT="Phrases for $CHAR on $DTE"
FILE="processed_${CHAR}_list_${DTE}"

cat $FILE | sendemail -l email.log -f $MY_EMAIL -u $SUBJECT -t $EXPERT_EMAIL -cc $CC -s $SMTP -o tls=yes -xu $MY_EMAIL -xp $PWD

cat $FILE

#4. file clean up
#rm linted_*.* unlinted_*.* unprocessed_*_list_* processed_*_list_*
