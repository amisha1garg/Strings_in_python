# Given a binary string S. The task is to count the number of substrings that start and end with 1. For example, if the input string is “00100101”, then there are three substrings “1001”, “100101” and “101”.
#
# Example 1:
#
# Input:
# N = 4
# S = 1111
# Output: 6
# Explanation: There are 6 substrings from
# the given string. They are 11, 11, 11,
# 111, 111, 1111.


# User function Template for python3

class Solution:

    # Function to count the number of substrings that start and end with 1.
    def binarySubstring(self, n, s):
        count = 0
        m = 0
        # code here
        for i in range(n):
            if s[i] == '1':
                m = m + 1

        return int((m * (m - 1)) / 2)


# {
#  Driver Code Starts
# Initial Template for Python 3

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


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        s = str(input())
        obj = Solution()
        print(obj.binarySubstring(n, s))
# } Driver Code Ends