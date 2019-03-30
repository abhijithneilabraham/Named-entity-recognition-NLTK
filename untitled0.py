#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 11:32:20 2019

@author: abhijithneilabraham
"""

from pattern.web import Twitter,plaintext
twitter=Twitter(language='en')
for tweet in twitter.search("kylie jenner",cached=False):
    print(plaintext(tweet.text))
