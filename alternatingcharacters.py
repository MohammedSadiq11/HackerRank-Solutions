#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count=0
    i=1
    for i in range(len(s)):
        if(i==len(s)-1):
            break
        if s[i]=='A':
            if s[i+1]=='B':
                continue
            else:
                count+=1
        if s[i]=='B':
            if s[i+1]=='A':
                continue
            else:
                count+=1

        
    return count
        

if __name__ == '__main__':
    

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print (result)
