# Given a list of names, display the longest name.
#
#
# Example:
#
# Input:
# N = 5
# names[] = { "Geek", "Geeks", "Geeksfor",
#   "GeeksforGeek", "GeeksforGeeks" }
#
# Output:
# GeeksforGeeks

# User function Template for python3

class Solution:
    def length(self, names, n):
        l = []
        for i in range(n):
            l.append(len(names[i]))
        return max(l)

    def longest(self, names, n):
        # code here
        for i in range(n):
            if len(names[i]) == Solution().length(names, n):
                return names[i]


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        names = []
        for i in range(n):
            names.append(input())
        ob = Solution()
        print(ob.longest(names, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends