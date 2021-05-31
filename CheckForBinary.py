# Given a non-empty sequence of characters str, return true if sequence is Binary, else return false
#
# Example 1:
#
# Input:
# str = 101
# Output:
# 1
# Explanation:
# Since string contains only 0 and 1, output is 1.

# Return true if str is binary, else false
def isBinary(s):
    # code here

    for i in range(len(s)):
        if s[i] not in ['0', '1']:
            return 0
    return 1


# {
#  Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        if isBinary(str):
            print(1)
        else:
            print(0)
# } Driver Code Ends