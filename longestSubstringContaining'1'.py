# Given a function that takes a binary string. The task is to return the longest size of contiguous substring containing only ‘1’.
#
# Input:
# The first line of input contains an integer T denoting the no of test cases.Then T test cases follow. Each test case contains a string S.
#
# Output:
# For each test case return the maximum length of required sub string.
#
# Constraints:
# 1<=T<=100
# 1<=|string length|<=104
#
# Example:
# Input:
# 2
# 110
# 11101110
# Output:
# 2
# 3

# User function Template for python3

def maxlength(s):
    # add code here
    count = 0
    x = s.split('0')
    # print(x)
    return len(max(x))
    # for i in range(len(s)):
    #     if s[i]=='1':
    #         count+=1
    #         continue
    #     if s[i]=='0':
    #         i=i+1
    #     m=count
    #     if m<count:
    #         m=count
    #     return m


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        print(maxlength(s))
# } Driver Code Ends