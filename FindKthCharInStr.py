# Given a decimal number m. Convert it into a binary string and apply n iterations, in each iteration 0 becomes 01, and 1 becomes 10. Find the kth (1-indexing) character in the string after nth iteration.
#
# Example 1:
#
# Input: m = 5, n = 2, k = 5
# output: 0
# Explanation: Binary represntation of m
# is "101", after one iteration binary
# reprentation will be "100110", and after
# second iteration binary repreentation
# will be "100101101001"


# User function Template for python3
class Solution:
    def kthCharacter(self, m, n, k):
        # code here
        M = str(bin(m))
        M = M[2:]

        for j in range(n):
            x = ""
            for i in range(len(M)):
                if M[i] == '0':
                    x += "01"
                elif M[i] == '1':
                    x += "10"


        j += 1
        M = x
        return M[k - 1]

# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        m, n, k = input().split()
        m, n, k = int(m), int(n), int(k)

        ob = Solution()
        answer = ob.kthCharacter(m, n, k)
        print(answer)

# } Driver Code Ends