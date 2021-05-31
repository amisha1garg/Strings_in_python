# Given a string S as input. Delete the characters at odd indices of the string.
#
# Example 1:
#
# Input: S = "Geeks"
# Output: "Ges"
# Explanation: Deleted "e" at index 1
# and "k" at index 3.

# User function Template for python3
class Solution:
    def delAlternate(ob, S):
        # code here
        new = ""
        for i in range(0, len(S)):
            if i % 2 == 0:
                new += S[i]

        return new


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.delAlternate(S))
# } Driver Code Ends