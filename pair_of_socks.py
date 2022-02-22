#!/bin/python3


import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar

from collections import Counter
def sockMerchant(n, ar):
    # n = int(input())
    c = Counter(map(int, ar))
    ans = 0
    for x in c:
        ans += c[x] // 2
    print(ans)
    # print(n)
    # print(ar)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)

    # fptr.write(str(result) + '\n')

    # fptr.close()