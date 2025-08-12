class Solution:
    def NnumbersSum(self, N):

        def fun(x):
            global count
            if x == 0:
                return 
            fun(x-1)
            count += x
        count = 0
        fun(n)
        print(count)
