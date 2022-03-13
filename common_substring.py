#!/bin/python3
import export as export





import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#
from collections import Counter
def twoStrings(s1, s2):
    for s in s1:
        if s in s2:
            return "YES"
            break
    return "NO"

    # Write your code here

if __name__ == '__main__':

    fptr = open('C:/Users/praveen/PycharmProjects/pythonProject/output', 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
