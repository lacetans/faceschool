faceschool
==========

Social network for educational institutions.

Important paths
/crear/ Leads you to a form in order to create a post. At the "name" field, you can write down
some profanities to see if the word filter does its job correctly. (IT'S JUST A SAMPLE FORM!).

/badwlist/ Leads you to a list, you can see there all the bad words entered in the database, plus you have quite more options! Enter a word, import a TXT file for a massive input of profanities, and remove from the registry the bad word that you want. You have exactly the same
functions in the /goodwlist/.

./imports 
That folder is where you can locate all the files that were uploaded via massive input.

./web/forms.py  
A simple form declaration for the /crear/ form

./web/badwords.txt 
A sample for the massive input

./web/goodworst.txt 
A sample for the massive input

./web/masive_filter.py 
That file opens the massive input file and then saves its content into a DB

./web/remove_filter.py 
Removes specific words from the DB

./web/word_filter.py 
That file is the filter itself. Compares a given string with a bad word,
if matches, then compares the word with a list of white list words, if matches again, the post will publizise, if not, then it will not save.
