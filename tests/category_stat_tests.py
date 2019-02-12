#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 17:34:37 2019

@author: seba
"""

import unittest
from category_stat import CategoryStat

class CategoryStatTests(unittest.TestCase):
    
    def testDemo(self):
        self.assertEqual('foo'.upper(), 'FOO');
    
    def shouldInit(self):
        simple = new CategoryStat('','','')
        self.assertEqual(simple, '')
    
        
if __name__ == '__main__':
    unittest.main()
