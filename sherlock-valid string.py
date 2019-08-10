#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    d=dict()
    s1="NO"
    s2="YES"
    count=0
    
    for x in s:
        if x in d:
            d[x]+=1
        else:
            d[x]=1
    lst=list(d.values())

    for i in range(0,len(lst)-1):
        if lst[i]==lst[i+1]:
            if(i==len(lst)-1):
                return s2
        elif lst[i]==lst[i+1]-1:
            lst[i+1]=lst[i+1]-1
            count+=1
            if count>1:
                return s1
        else:
            return s1
    if count>1:
        return s1
    else:
        return s2


    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
