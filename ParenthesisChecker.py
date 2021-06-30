# Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
# For example, the function should return 'true' for exp = “[()]{}{[()()]()}” and 'false' for exp = “[(])”.
#
# Example 1:
#
# Input:
# {([])}
# Output:
# true
# Explanation:
# { ( [ ] ) }. Same colored brackets can form
# balaced pairs, with 0 number of
# unbalanced bracket.


# User function Template for python3

class Solution:

    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        # code here
        stack = []
        close_list = ['}', ']', ')']
        open_list = ['{', '[', '(']

        for i in x:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if ((len(stack) > 0) and (open_list[pos] == stack[-1])):
                    stack.pop()
                else:
                    return 0

        if len(stack) == 0:
            return 1
        return 0


# {
#  Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        # n,k = map(int,imput().strip().split())
        # a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends