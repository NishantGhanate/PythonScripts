#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    count=n
    for i in range(n):
        for j in range(n):
            if j>=count-1:
                sys.stdout.write("#")
            else:
                sys.stdout.write(" ")
        count=count-1
        sys.stdout.write("\n")

if __name__ == '__main__':
    n = int(input())

    staircase(n)
