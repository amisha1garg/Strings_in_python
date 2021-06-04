# Given two strings S1 and S2 in lowercase, the task is to make them anagram. The only allowed operation is to remove a character from any string. Find the minimum number of characters to be deleted to make both the strings anagram. Two strings are called anagram of each other if one of them can be converted into another by rearranging its letters.
#
# Example 1:
#
# Input:
# S1 = bcadeh
# S2 = hea
# Output: 3
# Explanation: We need to remove b, c
# and d from S1.


# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
def remAnagram(str1, str2):
    # add code here
    list1 = list(str1)
    list2 = list(str2)
    list3 = []
    count = 0
    for each in list1:
        a = each
        if a in list2:
            list2.remove(a)
        else:
            count += 1
    count += len(list2)
    return count


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input()
        str2 = input()
        print(remAnagram(str1, str2))
# } Driver Code Ends