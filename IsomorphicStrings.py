# Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.
# Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible for every character of str1 to every character of str2 while preserving the order.
# Note: All occurrences of every character in ‘str1’ should map to the same character in ‘str2’
#
# Example 1:
#
# Input:
# str1 = aab
# str2 = xxy
# Output: 1
# Explanation: There are two different
# charactersin aab and xxy, i.e a and b
# with frequency 2and 1 respectively.


# User function Template for python3

class Solution:

    # Function to check if two strings are isomorphic.
    def areIsomorphic(self, s, p):
        return len(set(zip(s, p))) == len(set(s)) == len(set(p))


# {
#  Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        p = str(input())
        ob = Solution()
        if (ob.areIsomorphic(s, p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends