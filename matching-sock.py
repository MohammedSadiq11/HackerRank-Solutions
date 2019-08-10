#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d=dict()
    for x in ar:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1

    ans=0
    for x in d:
        if d[x]%2!=0:
            d[x]-=1
        ans+=d[x]/2
    return int(ans)

        

if __name__ == '__main__':
    

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print (result)
