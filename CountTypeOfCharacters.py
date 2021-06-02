# Given a string S, write a program to count the occurrence of Lowercase characters, Uppercase characters, Special characters and Numeric values in the string.
# Note: There are no white spaces in the string.
#
# Example 1:
#
# Input:
# S = "#GeeKs01fOr@gEEks07"
# Output:
# 5
# 8
# 4
# 2
# Explanation: There are 5 uppercase characters,
# 8 lowercase characters, 4 numeric characters
# and 2 special characters.

# User function Template for python3

class Solution:
    def count(self, s):
        # your code here
        num = 0
        l = 0
        u = 0
        sp = 0
        for i in s:
            if i.isupper():
                u += 1
            elif i.islower():
                l += 1

            elif i.isdigit():
                num += 1

            else:
                sp += 1

        return u, l, num, sp


# {
#  Driver Code Starts
# Initial Template for Python 3

t = int(input())
for tc in range(t):
    s = input()
    ob = Solution()
    res = ob.count(s)

    for i in res:
        print(i)

# Contributed By: Pranay Bansal

# } Driver Code Ends