#!/bin/python

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(m, n, queries):
    x=list()
    for i in range(n):
        x.append(0)
    for y in range(m):
        for i in range(queries[y][0]-1,queries[y][1]):
            x[i]=x[i]+queries[y][2]
    return max(x)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(m, n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
