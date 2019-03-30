#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 01:09:05 2019

@author: abhijithneilabraham
"""

from geotext import GeoText
places = GeoText("Delhi is not near")
print(places.cities)

c=10
if c>5:
    print("")
else:
    print("no")