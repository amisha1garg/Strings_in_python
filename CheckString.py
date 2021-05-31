# Given a string, check if all its characters are same or not.
# 
# Example 1:
# 
# Input:
# s = "geeks"
# Output: NO
# Explanation: The string contains different
# character 'g', 'e', 'k' and 's'.

# User function Template for python3

class Solution:
    def check(self, s):
        # your code here
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                return False
        return True


# {
#  Driver Code Starts
# Initial Template for Python 3

t = int(input())
for tc in range(t):
    s = input()
    ob = Solution()
    if ob.check(s):
        print("YES")
    else:
        print("NO")

# Contributed By: Pranay Bansal

# } Driver Code Ends