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
from forms import RemovebadwForm
from forms import RemovegoodwForm
from forms import BadwmasivaForm
from forms import GoodwmasivaForm
from web.models import Post
from web.models import Badws
from web.models import Goodws
from web.models import Removebadws
from web.models import Removegoodws
from web.models import Badwsmasiva
from web.models import Goodwsmasiva

def bremove_filter(message):
    
    message = str(message)
    obj = Badws.objects.filter(texto=message)        
    for row in obj:
        row.delete()

def gremove_filter(message):
    
    message = str(message)
    obj = Goodws.objects.filter(texto=message)        
    for row in obj:
        row.delete()
    
