# -*- coding: utf-8 -*-
"""
Created on Sat May 15 17:08:01 2021

@author: Sergio
"""

import requests

def insertPost(values):
    res = requests.post('http://conisoft.org/FacebookScraper/insertPost.php', data=values)
    return res.text

def insertComment(values):
    res = requests.post('http://conisoft.org/FacebookScraper/insertComment.php', data=values)
    return res.text