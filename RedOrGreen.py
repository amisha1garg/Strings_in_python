# Given a string of length N, made up of only uppercase characters 'R' and 'G', where 'R' stands for Red and 'G' stands for Green.Find out the minimum number of characters you need to change to make the whole string of the same colour.
#
# Example 1:
#
# Input:
# N=5
# S="RGRGR"
# Output:
# 2
# Explanation:
# We need to change only the 2nd and
# 4th(1-index based) characters to 'R',
# so that the whole string becomes
# the same colour.

# User function Template for python3

class Solution:
    def RedOrGreen(self, N, S):
        # code here
        R = 0
        G = 0
        for i in range(N):
            if S[i] == 'R':
                R += 1
            if S[i] == 'G':
                G += 1
        return min(R, G)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()

        ob = Solution()
        print(ob.RedOrGreen(N, S))
# } Driver Code Ends