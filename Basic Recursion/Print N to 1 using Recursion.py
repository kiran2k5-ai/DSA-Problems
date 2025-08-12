class Solution:
    def printNumbers(self, n):

        def fun(x):
            if x > 0:
                print(x)
                fun(x-1)
            else:
                return 
        fun(n)
