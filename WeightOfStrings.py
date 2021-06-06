# You are given two strings S1 and S2. You need to find weights of both strings and compare them. The weight of a string can be obtained by adding individual weights of the characters that make the string. The weight of individual characters are the position on which they occur in the english alphabets table; for eg, a has weight 1, z has weight 26.
#
# Input:
# The first line of the input contains a single integer T, denoting the number of test cases. Then T test cases follow. Each testcase has 2 lines
# The first string S1
# The second string S2
#
# Output:
# Print 1 if the weight of the first string is greater. Print 2 if the weight of the second string is greater. Print equal if the the weights are equal.
#
# Constraints:
# 1<=T<=100
# 1<=|S1|<=1000
# 1<=|S2|<=1000
#
# Example:
#
# Input:
# 4
# batman
# superman
# kira
# l
# goku
# broly
# manbat
# batman
#
# Output:
# 2
# 1
# 2
# equal

# code
t = int(input())
for i in range(t):
    s1 = input()
    s2 = input()
    c1 = 0
    c2 = 0
    for j in range(len(s1)):
        c1 += ord(s1[j]) - 96
    for j in range(len(s2)):
        c2 += ord(s2[j]) - 96
    if c1 > c2:
        print(1)
    elif c2 > c1:
        print(2)
    else:
        print("equal")

