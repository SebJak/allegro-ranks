import json
from category_list import CategoryList
from allegro_client import AllegroClient
from offer import Offer

#with open('../sample/categories.json.sample', 'r') as f: ##We can replace it with StringIO(fileName)
#	categoriesFromFile = json.load(f)
#
#allegroCategories = CategoryList(categoriesFromFile['categories'])
#
#for mycategory in allegroCategories.categories:
#    print(mycategory)
#    
#with open('../sample/offers.json.sample', 'r') as jsonOffers:
#    offersFromFile = json.load(jsonOffers)
#
#items = [];
#
#for item in offersFromFile['items']['regular']:
#    items.append(Offer(item))
try:
    with open('credentials.json', 'r') as f:
        credentials = json.load(f)
except FileNotFoundError:
    raise EnvironmentError("No such file or directory: 'credentials.json. Please create credential file as example from ../sample/")
    
allegroClient = AllegroClient(credentials['env'], credentials['clientId'], credentials['secret'])

response = allegroClient.get('/offers/listing?category.id=4694&limit=10')
        