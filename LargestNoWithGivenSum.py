# Geek lost the password of his super locker. He remembers the number of digits N as well as the sum S of all the digits of his password. He know that his password is the largest number of N digits that can be made with given sum S. As he is busy doing his homework, help him retrieving his password.
#
# Example 1:
#
# Input:
# N = 5, S = 12
# Output:
# 93000
# Explanation:
# Sum of elements is 12. Largest possible
# 5 digit number is 93000 with sum 12.

# User function Template for python3

class Solution:
    # Function to return the largest possible number of n digits
    # with sum equal to given sum.
    def largestNum(self, n, s):

        # code here
        if s > 9 * n:
            return -1
        new = ""
        for i in range(n):
            if s >= 9:
                new += "9"
                s -= 9
            else:
                new += str(s)
                s -= s

        return new


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, s = map(int, input().strip().split())
        ob = Solution()
        print(ob.largestNum(n, s))
# } Driver Code Ends