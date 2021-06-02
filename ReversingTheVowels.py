# Given a string consisting of lowercase english alphabets, reverse only the vowels present in it and print the resulting string.
#
# Example 1:
#
# Input:
# S = "geeksforgeeks"
# Output: geeksforgeeks
# Explanation: The vowels are: e, e, o, e, e
# Reverse of these is also e, e, o, e, e.

#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        p=['a','e','i','o','u']
        t=''
        for i in s:
            if i in p:
                t=t+i
        t=t[::-1]
        r=0
        s1=[]
        for i in s:
            s1.append(i)
        for i in range(len(s)):
            if s1[i] in p:
                s1[i]=t[r]
                r+=1
        return "".join(s1)

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends