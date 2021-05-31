# Given a String S , print the reverse of the string as output.
#
# Example 1:
#
# Input: S = "GeeksforGeeks"
# Output: "skeeGrofskeeG"
# Explanation: Element at first is at last and
# last is at first, second is at second last and
# second last is at second position and so on .

# User function Template for python3
class Solution:
    def revStr(ob, S):
        # code here

        return S[::-1]


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.revStr(S))
# } Driver Code Ends