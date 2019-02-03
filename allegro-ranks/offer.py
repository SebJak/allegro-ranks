#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 10:14:15 2019

@author: seba
"""
class Offer(object):
    def __init__(self, attributes):
        self.name = attributes['name']
        self.id = attributes['id']
        self.seller = attributes['seller']
        self.sellingMode = attributes['sellingMode']
        self.stock = attributes['stock']
        
    def __str__(self):
        return "Offer: " + self.name + ", price: " + self.sellingMode
