# Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, “act” and “tac” are an anagram of each other.
#
# Example 1:
#
# Input:
# a = geeksforgeeks, b = forgeeksgeeks
# Output: YES
# Explanation: Both the string have same
# characters with same frequency. So,
# both are anagrams.


# User function Template for python3


class Solution:

    # Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
        # code here
        a = [i for i in a]
        b = [i for i in b]
        a.sort()
        b.sort()
        if a == b:
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
    t = int(input())
    for i in range(t):
        a, b = map(str, input().strip().split())
        if (Solution().isAnagram(a, b)):
            print("YES")
        else:
            print("NO")
            # } Driver Code Ends