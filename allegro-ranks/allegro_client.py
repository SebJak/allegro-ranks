#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 15:10:18 2019

@author: seba
"""
import requests, json

class AllegroClient(object):
            
    def __init__(self, url, clientId, secret):
        print('AllegroClient '+ clientId + ' ' + secret)
        self.url = url
        self.clientId = clientId
        self.secret = secret
        self.access_tocken = self.__getAccessToken(clientId, secret)
        
    def __str__(self):
        return self.url
    
    def get(self, path):
        headers = {'Authorization': 'Bearer' + self.access_tocken, 'Accept': 'application/vnd.allegro.public.v1+json'}
        print("access_tocken: " + self.access_tocken + 'url: ' + self.url + path)
        response = requests.get(self.url + path, headers=headers)
        if(response.status_code == 200):
            return json.loads(response.content)
        raise ConnectionError('Error during geting data from: ' + self.url + path + ' Status code: ' + response.status_code)
        
    def __getAccessToken(self, clientId, secret): #TODO we should have the dynamic auth address depend on env
        response = requests.post('https://allegro.pl.allegrosandbox.pl/auth/oauth/token?grant_type=client_credentials',\
                                 auth=(clientId, secret))
        if(response.status_code == 200):
            return json.loads(response.text)['access_token']
        raise ConnectionError(response.text)
        
    def __refreshToken(self): #TODO needs to be implemented
        raise Exception('Not implemented')