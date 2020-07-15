# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:15:14 2020

@author: Administrator
"""
import os
import sys

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


print('1')

blockPrint()
print('2')

enablePrint()
print('3')