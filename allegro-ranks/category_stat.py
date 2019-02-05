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
        
    def __str__(self):
        return "CategoryStat: " + self.name + ":"+ self.id + " , totalCount: " + self.totalCount
    
    def __iter__(self):
        return iter([self.id, self.name, self.availableCount, self.totalCount])
    
    def asCsvRow(self):
        return [self.id, self.name, self.availableCount, self.totalCount]
