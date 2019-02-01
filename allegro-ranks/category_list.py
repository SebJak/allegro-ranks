#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:21:08 2019

@author: seba
"""

from category import Category

class CategoryList(list):
    def __init__(self, objectsList):
        self.categories = [];
        for category in objectsList:
            self.categories.append(Category(category))
            
    def __str__(self):
        return self.categories