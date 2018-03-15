#!/bin/python3

import os
import sys

berth = ['SUB', 'LB', 'MB', 'UB', 'LB', 'MB', 'UB', 'SLB']
#
# Complete the berthType function below.
#
def berthType(n):
    return berth[n%8]



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = berthType(n)

    f.write(result + '\n')

    f.close()
