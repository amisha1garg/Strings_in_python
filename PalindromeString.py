# Given a string S, check if it is palindrome or not.
#
# Example 1:
#
# Input: S = "abba"
# Output: 1
# Explanation: S is a palindrome

#User function Template for python3
class Solution:
	def isPlaindrome(self, S):
		# code here
		x=S[:][::-1]
		if x==S:
		    return 1
	    return 0

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPlaindrome(S)
		print(answer)

# } Driver Code Ends