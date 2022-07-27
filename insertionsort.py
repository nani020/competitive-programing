import math
import os
import random
import re
import sys

def insertionSort(array):
    
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
     
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            print(*data, sep = ' ')

            
        array[j + 1] = key
n=int(input())
data=[int(i) for i in input().split()]

insertionSort(data)
print(*data, sep = ' ')

