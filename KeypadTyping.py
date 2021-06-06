# You are given a string S of alphabet characters and the task is to find its matching decimal representation as on the shown keypad. Output the decimal representation corresponding to the string. For ex: if you are given “amazon” then its corresponding decimal representation will be 262966.
#
#
#
# Example 1:
#
# Input:
# S = geeksforgeeks
# Output: 4335736743357
# Explanation:geeksforgeeks is 4335736743357
# in decimal when we type it using the given
# keypad.

# User function Template for python3


# Function to find matching decimal representation of a string as on the keypad.
def printNumber(s, n):
    # CODE HERE
    x = ''
    for i in range(len(s)):
        if s[i] in ['a', 'b', 'c']:
            x += '2'
        elif s[i] in ['d', 'e', 'f']:
            x += '3'
        elif s[i] in ['g', 'h', 'i']:
            x += '4'
        elif s[i] in ['j', 'k', 'l']:
            x += '5'
        elif s[i] in ['m', 'n', 'o']:
            x += '6'
        elif s[i] in ['p', 'q', 'r', 's']:
            x += '7'
        elif s[i] in ['t', 'u', 'v']:
            x += '8'
        elif s[i] in ['w', 'x', 'y', 'z']:
            x += '9'
    return x


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        print(printNumber(s, n))
# } Driver Code Ends