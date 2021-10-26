# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 10:25:27 2021

@author: anaca
"""

def bubbleSort(lista):
    stop=1
    while stop==1:
        stop=0
        i=0
        while i<len(lista)-1:
            if lista[i]>lista[i+1]:
                temp=lista[i+1]
                lista[i+1]=lista[i]
                lista[i]=temp
                i=i+1
                stop=1
            else:
                i=i+1
    return lista
