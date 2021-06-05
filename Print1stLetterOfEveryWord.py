# Given
# a
# string
# S, the
# task is to
# create
# a
# string
# with the first letter of every word in the string.
#
# Example
# 1:
#
# Input:
# S = "geeks for geeks"
# Output: gfg

# User function Template for python3
class Solution:
    def firstAlphabet(self, S):
        # code here
        x = S.split(" ")
        c = ""
        for i in range(len(x)):

    c += x[i][0]
    return c


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.firstAlphabet(S)

        print(answer)

# } Driver Code Ends