import json;
from category_list import CategoryList;
            
def jsonDefault(object):
    return object.__dict__

with open('sample-categories.json', 'r') as f: ##We can replace it with StringIO(fileName)
	categoriesFromFile = json.load(f)

allegroCategories = CategoryList(categoriesFromFile['categories'])

for mycategory in allegroCategories.categories:
    print(mycategory)
        