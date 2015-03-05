__author__ = 'joaquin'
from web.models import FSUser
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import csv
import os.path
import sys
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

class Command(BaseCommand):

    def handle(self, *args, **options):

        csv_filepathname = args[0]
        sys.path.append(PROJECT_ROOT)
        dataReader = csv.reader(open(csv_filepathname), delimiter=';', quotechar='"')
        i = 0
        index = {}
        for row in dataReader:
            if i==0:
                index = self.comprovaCamps(row)
            else:
                usuari = User()
                name = row[index.get('Name')]
                surname = row[index.get('Surname')]
                email = row[index.get('E-mail')]

                username = self.comprovaUser(name, surname, email, usuari)
                if(username!=False):
                    usuari.email = row[index.get('E-mail')]
                    usuari.username = username
                    usuari.first_name = row[index.get('Name')]
                    usuari.last_name = row[index.get('Surname')]
                    #usuari.FSUser._class = row[index.get('Class')]
                    usuari.save()


            i += 1
    def comprovaUser(self, name, surname, email, usuari):

        surname = surname.replace(" ", "")
        username = surname+name
        raw_input("""""")
        totalUsers = User.objects.all()

        print totalUsers


        for usr in totalUsers:

            if(usr.username==username):
                if(usr.email==email):
                    return False
                else:
                    surname = surname+name+str(1)
                    return surname

        return username

    def comprovaCamps(self, row):

        row = ';'.join(row)

        email = row.find("E-mail")
        _class = row.find("Class")
        surname = row.find("Surname")
        name = row.find("Name")



        if(email <= -1):
            print """Error: E-mail not found """
            return 0
        elif(_class <= -1):
            print """Error: Classroom not found """
            return 0
        elif(name <= -1):
            print """Error: Name not found"""
            return 0
        elif(surname <= -1 ):
            print """Error: Surname and Name not found """
            return 0

        else:
            row = row.split(";")
            print row
            index = {}
            i = 0
            for i in range(len(row)):
                index[row[i]] = i
            print index
            print row


        return index




