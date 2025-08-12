class Solution:
    def printNumbers(self, n):

        def fun(x):
          print(x)
        count = 1
        while count <= n:
          fun(count)
          count += 1
