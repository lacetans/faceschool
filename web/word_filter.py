#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import codecs
from forms import PostForm
from forms import BadwForm
from forms import GoodwForm
from web.models import Post
from web.models import Badws
from web.models import Goodws

class Filter(object):
    def __init__(self, badWords, goodWords, publish):
        """
        publish: publish the comment -- yes/no
        badWords: words forbidden -- external file
        goodWords: words allowed -- external file
        """
        self.badWords = badWords
        self.goodWords = goodWords
        self.publish = publish

    def clean(self, text):
        """
        Converts both dictionary into two strings
        Find all the matches and replace every word with ''
        Compares the string with a list of bad words and a list of exceptions
        """
        regexp = '|'.join(self.badWords)
        rbad = re.compile(regexp, re.IGNORECASE)
        rbad = rbad.sub('', text)
        regexpx = '|'.join(self.goodWords)
        rgood = re.compile(regexpx, re.IGNORECASE)
        rgood = rgood.sub('', text)
        if ((text != rbad)and(text == rgood)):
            self.publish = "no"
        return text

def language_filter(text):
    goodWords = []
    badWords = []
    lines_in_badwords = Badws.objects.values('texto')
    i = 0
    for line in lines_in_badwords:
        badWords.append(lines_in_badwords[i]['texto'].encode('utf-8'))
        i = i +1
            
    lines_in_goodwords = Goodws.objects.values('texto')
    j = 0
    for line in lines_in_goodwords:
        goodWords.append(lines_in_goodwords[j]['texto'].encode('utf-8'))
        j = j +1
    publish = "yes"
   
    f = Filter(badWords,goodWords,publish)
    text = text.rstrip('\n')
    fclean = f.clean(text)
    publish = f.publish
    return publish
