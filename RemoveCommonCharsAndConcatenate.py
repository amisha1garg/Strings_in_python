# Given two strings s1 and s2. Modify both the strings such that all the common characters of s1 and s2 are to be removed and the uncommon characters of s1 and s2 are to be concatenated.
# Note: If all characters are removed print -1.
#
# Example 1:
#
# Input:
# s1 = aacdb
# s2 = gafd
# Output: cbgf
# Explanation: The common characters of s1
# and s2 are: a, d. The uncommon characters
# of s1 and s2 are c, b, g and f. Thus the
# modified string with uncommon characters
# concatenated is cbgf.


# User function Template for python3

class Solution:

    # Function to remove common characters and concatenate two strings.
    def concatenatedString(self, s1, s2):
        # code here
        r = ""
        for i in range(len(s1)):
            if s1[i] not in s2:
                r += s1[i]
        for i in range(len(s2)):
            if s2[i] not in s1:
                r += s2[i]
        if len(r) > 0:
            return r
        else:
            return -1


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
        s = str(input())
        p = str(input())
        obj = Solution()
        print(obj.concatenatedString(s, p))
# } Driver Code Ends