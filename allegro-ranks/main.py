import json
import csv
import datetime

from category_list import CategoryList
from allegro_client import AllegroClient
from category_stat import CategoryStat
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

now = datetime.datetime.now()

try:
    with open('credentials.json', 'r') as f:
        credentials = json.load(f)
except FileNotFoundError:
    raise EnvironmentError("No such file or directory: 'credentials.json. Please create credential file as example from ../sample/")
    
allegroClient = AllegroClient(credentials['env'], credentials['clientId'], credentials['secret'])

categories = CategoryList(allegroClient.get('/categories')['categories'])

categoriesStats = [['CategoryId', 'Name', 'Path', 'AvailableCount', 'TotalCount']]
#
print('Categories count:', len(categories.categories)) #31017 sandbox 24096 prod
with open('../data/categoryStats'+str(now)+'.csv', 'w') as csv_file:
    wr = csv.writer(csv_file, delimiter=',')
    wr.writerows(categoriesStats)
    for category in categories.categories:
        try:
            stat = CategoryStat(category.id, category.name, allegroClient.get('/offers/listing?category.id=' + category.id + '&limit=1'))
            print(stat.name)
            wr.writerow(stat.asCsvRow())
        except Exception as ex:
            print("Exception during processing data for category:" + category.name + ":"+ category.id +" "+ format(ex))

#with open('../sample/offers-sample.json', 'r') as jsonOffers:
#    offersFromFile = json.load(jsonOffers)
#
#stat = CategoryStat('4694', 'Electronicka', offersFromFile)
#categoriesStats.append(stat.asCsvRow())

csv_file.close();
        


#TODO
# read all categories from allegro
# iterate over categories and read data from there
# save to csv file
        