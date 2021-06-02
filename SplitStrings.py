# Given a string S which consists of alphabets , numbers and special characters. You need to write a program to split the strings in three different strings S1, S2 and S3 such that the string S1 will contain all the alphabets present in S , the string S2 will contain all the numbers present in S and S3 will contain all special characters present in S.  The strings S1, S2 and S3 should have characters in same order as they appear in input.
#
#
# Example 1:
#
# Input:
# S = geeks01for02geeks03!!!
# Output:
# geeksforgeeks
# 010203
# !!!
# Explanation: The output shows S1, S2 and S3.

# User function Template for python3

class Solution:
    def splitString(ob, S):
        # code here
        s1 = ""
        s2 = ""
        s3 = ""
        for char in S:
            if char.isalpha():
                s1 += char
            elif char.isdigit():
                s2 += char
            else:
                s3 += char
        return s1, s2, s3


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        ans = ob.splitString(S)
        for i in ans:
            if (i == ""):
                print(-1)
            else:
                print(i)

# } Driver Code Ends