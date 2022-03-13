#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#
from collections import Counter
def checkMagazine(magazine, note):
    # note = list()
    # magazine = list()
    # for i in note:
    #     if i in magazine:
    #         magazine.remove(i)
    #     else:
    #         return "NO"
    # return "YES"
    nc = Counter(note)
    mc = Counter(magazine)
    if len(nc) > len(mc):
        return "No"
    # print(nc, mc)
    for word in nc:
        if word in mc:
            if int(mc[word]) < int(nc[word]):
                return "No"
        else:
            return "No"
    return "Yes"


    # for i in nc:
    #     if



    # Write your code


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))


# def ransom_note(magazine, ransom):
#     rc = {}  # dict of word: count of that word in the note
#     for word in ransom:
#         if word not in rc:
#             rc[word] = 0
#         rc[word] += 1
#         print(rc)
#
#     for word in magazine:
#         if word in rc:
#             rc[word] -= 1
#             if rc[word] == 0:
#                 del rc[word]
#                 if not rc:
#                     return True
#     return False
#
#
# m, n = map(int, input().strip().split(' '))
# magazine = input().strip().split(' ')
# ransom = input().strip().split(' ')
# answer = ransom_note(magazine, ransom)
# if (answer):
#
#     print("Yes")
# else:
#     print("No")