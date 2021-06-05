# Given a number as string(n) , find the remainder of the number whe it is divided by 7
#
# Example 1:
#
# Input:
# 5
# Output:
# 5


class Solution:
    #your task is to complete this function
    #Function should return the required answer
    #You are not allowed to convert string to integer
    def remainderWith7(self, str):
        #Code here
        str1= int(str)
        return str1%7
#{
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        ob=Solution()
        print(ob.remainderWith7(str))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends