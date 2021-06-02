# Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating another string 'a' by exactly 2 places.
#
# Example 1:
#
# Input:
# a = amazon
# b = azonam
# Output: 1
# Explanation: amazon can be rotated anti
# clockwise by two places, which will make
# it as azonam.

#User function Template for python3


class Solution():
#Function to check if a string can be obtained by rotating
#another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        str3=""
        str4=""
        str3 += str1[2:] + str1[:2]
        str4 += str1[-2:] + str1[:-2]
        if str2==str3 or str2==str4:
            return 1
        return 0

#{
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        if(Solution().isRotated(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends