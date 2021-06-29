# Given a string S contains 0's, 1's, and 2's, the task is to find the number of goals on the penalty.
#
#  '1' stands for "goal".
#  '0' stands for "no goal".
#  '2' stands for a foul which gives a penalty.
# Example 1:
#
# Input: S = "1012012112110"
# Output: 2
# Explanation: There are 3 penalties,
# of which he scores only 2.
# 1012012112110

# User function Template for python3
class Solution:
    def penaltyScore(self, s):
        # code here
        c = 0
        for i in range(len(s) - 1):
            if s[i] == "2":
                if s[i + 1] == "1":
                    c += 1

    return c


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.penaltyScore(S)

        print(answer)

# } Driver Code Ends