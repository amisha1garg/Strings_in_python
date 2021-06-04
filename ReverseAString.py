# You are given a string s. You need to reverse the string.
#
# Example 1:
#
# Input:
# s = Geeks
# Output: skeeG

#User function Template for python3

def reverseWord(s):
    #your code here
    s1=""
    for i in s[::-1]:
        s1+=i
    return s1

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends