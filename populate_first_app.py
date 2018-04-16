import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord,Webpage,Topic

from faker import Faker

fakegen = Faker()
topics = ['search', 'social', 'news', 'marketplace', 'games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):

        #get topic entry for the entry
        top = add_topic()

        #create the data for that entry
        fake_name = fakegen.company()
        fake_date = fakegen.date()
        fake_url = fakegen.url()


        #create the new entry for webpage
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create the fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]



if __name__=='__main__':
      print('populating data')
      populate(20)
      print('populating complete')