#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:06:55 2019

@author: seba
"""

class CategoryStat(object):
    def __init__(self, categoryId, name, attributes):
        self.name = name
        self.id = categoryId
        self.availableCount = attributes['searchMeta']['availableCount']
        self.totalCount = attributes['searchMeta']['totalCount']
        self.path = ''
        self.tags = []
        for path in attributes['categories']['path']: #TODO Please make it as ('/').join(collection)
            self.path += path['name'] +'/'
            self.tags.append(path['name'])
        print(self.path)
        
    def __str__(self):
        return "CategoryStat: " + self.name + ":"+ self.id + " , totalCount: " + self.totalCount
    
    def __iter__(self):
        return iter([self.id, self.name, self.path, self.availableCount, self.totalCount])
    
    def asCsvRow(self):
        return [self.id, self.name, self.path, self.availableCount, self.totalCount]

    def model(self): #https://stackoverflow.com/questions/26712080/python-decision-tree-classification-of-complex-objects
        #Tags needs to be represented as a single valu which can be compare with another objects
        return [selgf.id, self.tags, selg.totalCount]
    

import unittest
class CategoryStatTests(unittest.TestCase):
    
    #def testDemo(self):
        #self.assertEqual('foo'.upper(), 'FOO');
    
    def test_shouldInit(self):
        #Given
        attributes = {
                'searchMeta': {
                        'availableCount': 10,
                        'totalCount': 15 
                        },
                'categories': {
                        'path': [{'name': 'Allegro'}, {'name': 'Category'}]
                        }
                }
        #When
        simple = CategoryStat('categoryId','Category', attributes)
        
        #Then
        self.assertEqual(simple.name, 'Category1')
    
        
if __name__ == '__main__':
    unittest.main()
