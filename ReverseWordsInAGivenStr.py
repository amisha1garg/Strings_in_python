# Given a String S, reverse the string without reversing its individual words. Words are separated by dots.
#
# Example 1:
#
# Input:
# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
# Explanation: After reversing the whole
# string(not individual words), the input
# string becomes
# much.very.program.this.like.i


# User function Template for python3

class Solution:

    # Function to reverse words in a given string.
    def reverseWords(self, S):
        # code here
        y = []
        x = list(S.split("."))
        x.reverse()
        return ".".join(x)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends