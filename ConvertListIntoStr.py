# Given a list of characters, merge all of them into a string.
#
# Example 1:
#
# Input:
# N = 13
# Char array = g e e k s f o r g e e k s
# Output: geeksforgeeks
# Explanation: combined all the characters
# to form a single string.


#User function Template for python3

class Solution:
    def chartostr(self, arr,N):
        # code here
        new = ""
        for x in arr:
            new+=x
        return new

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        N= int(input())
        arr =input().split()
        ob = Solution()
        print(ob.chartostr(arr,N))
# } Driver Code Ends