

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minmax=[]
    tra=0
    for i in range(0,len(arr)):
        minmax.append(sum(arr)-arr[i])
    print(min(minmax),end=" ")
    print(max(minmax),end="")   

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)