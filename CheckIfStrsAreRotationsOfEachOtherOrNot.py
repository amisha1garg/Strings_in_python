# Given
# two
# strings
# s1 and s2.The
# task is to
# check if s2 is a
# rotated
# version
# of
# the
# string
# s1.The
# characters in the
# strings
# are in lowercase.
#
# Example
# 1:
#
# Input:
# geeksforgeeks
# forgeeksgeeks
# Output:
# 1
# Explanation: s1 is geeksforgeeks, s2 is
# forgeeksgeeks.Clearly, s2 is a
# rotated
# version
# of
# s1 as s2
# can
# be
# obtained
# by
# left - rotating
# s1
# by
# 5
# units.


# User function Template for python3

class Solution:

    # Function to check if two strings are rotations of each other or not.
    def areRotations(s1, s2):
        # code here
        if (len(s1)) != len(s2):
            return 0
        s1 += s1
        if s1.find(s2) >= 0:
            return 1
        return 0


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
    t = int(input("t "))
    for i in range(t):
        s1 = str(input("s1 "))
        s2 = str(input("s2"))
        if (Solution().areRotations(s1,s2)):
            print(1)
        else:
            print(0)

# } Driver Code Ends