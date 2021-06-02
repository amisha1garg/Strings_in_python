# Remove all characters except the numeric characters from an alphanumeric string.
#
# Example 1:
#
# Input: S = "AA1d23cBB4"
# Output: 1234
# Explanation: Remove all chacactres
# other than numbers

# User function Template for python3
class Solution:
    def removeCharacters(self, S):
        # code here
        new = ""

    for i in S:
        if i.isdigit():
            new += i
    return new


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeCharacters(s)

        print(answer)

# } Driver Code Ends