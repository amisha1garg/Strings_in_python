# # Given an integer n, your task is to complete the function convertToRoman which prints the corresponding roman number of n. Various symbols and their values are given below.
# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000
#
# Example
# 1:
#
# Input:
# n = 5
# Output: V


# Your task is to complete this function
# Your function should return a String
def convertRoman(num):
    # Code here
    # Python3 program for above approach

    # Function to calculate roman equivalent

    # Storing roman values of digits from 0-9
    # when placed at different places
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    # Converting to roman
    thousands = m[num // 1000]
    hundereds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]

    ans = (thousands + hundereds +
           tens + ones)

    return ans;


# Driver code


#


# {
#  Driver Code Starts
# Your Code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(convertRoman(n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends