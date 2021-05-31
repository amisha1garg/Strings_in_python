# Given a string, remove the vowels from the string.
#
# Example 1:
#
# Input: S = "welcome to geeksforgeeks"
# Output: wlcm t gksfrgks
# Explanation: Ignore vowels and print other
# characters

# User function Template for python3
class Solution:
    def removeVowels(self, S):

    # code here
    S2 = ""
    for variable in (S):
        if variable not in "aeiouAEIOU":
            S2 = S2 + variable
    return S2


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeVowels(s)

        print(answer)

# } Driver Code Ends