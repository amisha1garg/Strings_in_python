# Given a string S of lowercase alphabets, check if it is isogram or not. An Isogram is a string in which no letter occurs more than once.
#
# Example 1:
#
# Input:
# S = machine
# Output: 1
# Explanation: machine is an isogram
# as no letter has appeared twice. Hence
# we print 1.


# User function Template for python3

class Solution:

    # Function to check if a string is Isogram or not.
    def isIsogram(self, s):
        # Your code here
        a = list(s)
        if len(set(a)) == len(a):
            return True
        else:
            return False


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())

    while (T > 0):

        s = input()
        obj = Solution()
        if obj.isIsogram(s) is True:
            print(1)
        else:
            print(0)
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends