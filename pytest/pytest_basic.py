#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:58:27 2021

@author: kishore7
"""


import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5
   assert math.sqrt(num) == 6

def test_square():
   num = 7
   assert 7*7 == 49
   
def test_equality():
   assert 10 == 10