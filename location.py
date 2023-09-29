import time
from models import *
from utils import *
from instagrapi import Client
from ensta import Guest

#guest = Guest()
cl = Client()
cl.load_settings("session.json")
cl.login("unknownmani.ki", "7DYZ7BM8YKa7Apb")
cl.get_timeline_feed() # check session



location = cl.location_search(6.5244, 3.3792)[0]
location_id = location.dict()['external_id']



print(location_id)
time.sleep(1)
#medias = cl.location_medias_top(location_id, amount=2)

#print(medias[0].dict())
