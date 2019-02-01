#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:07:48 2019

@author: seba
"""

class Category(object):
    def __init__(self, attributes):
        self.name = attributes['name']
        self.id = attributes['id']
        
    def __str__(self):
        return "Category: " + self.name + ", Id: " + self.id
