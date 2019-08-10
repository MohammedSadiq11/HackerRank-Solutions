#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n,c):
    count=0
    x=0
    while x<n-1:
        if x==n-2:
            count+=1
            break

        elif c[x+2]==1:
            x+=1
            count+=1
        else:
            x+=2
            count+=1

    return count

    

if __name__ == '__main__':
    

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n,c)

    print (result)
