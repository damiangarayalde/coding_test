#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if len(s)==10:
        descriptor = s[-2:]
        hour = (int(s[:2]))

        if descriptor == 'AM':
            if hour >= 12: 
                hour = hour -12
        else:
            if hour < 12: 
                hour = hour +12
        
        return  f"{hour:02}"+s[2:-2]
    # Write your code here
    else: 
        return 'Incorrect amount of characters'

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = '07:45:54PM' #input()

    result = timeConversion(s)

    print(result)
    #fptr.write(result + '\n')

   # fptr.close()