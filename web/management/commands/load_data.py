__author__ = 'joaquin'
from models import FSUser
import csv
import os.path
import sys
from django.db import models

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.append(PROJECT_ROOT)
#os.environ['DJANGO_SETTINGS_MODULE'] = 'faceschool.settings'


csv_filepathname = PROJECT_ROOT+"/web/usuaris.csv"

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
for row in dataReader:
    if row[0] != "username":
        FSUser = FSUser()
        FSUser.user.username = row[0]
        FSUser.user.first_name = row[1]
        FSUser.user.last_name = row[2]
        FSUser.user.email = row[3]
        FSUser.save()