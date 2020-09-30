import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    minimum = max(arr)
    maximum = min(arr)
    a = sum(arr) - maximum
    b = sum(arr) - minimum
    print(f'{b} {a}')

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
