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
from forms import BadwmasivaForm
from forms import GoodwmasivaForm
from web.models import Post
from web.models import Badws
from web.models import Goodws
from web.models import Badwsmasiva
from web.models import Goodwsmasiva

def bmasive_upload_filter(archivo):
    lines = archivo.read().replace('\r\n','')
    lines = lines.split(',')
    for line in lines:
        Badws.objects.create(texto=line)

def gmasive_upload_filter(archivo):
    lines = archivo.read().replace('\r\n','')
    lines = lines.split(',')
    for line in lines:
        Goodws.objects.create(texto=line)
    
