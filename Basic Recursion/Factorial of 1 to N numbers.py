class Solution:
    def Factorial(self, N):
        
        def fun(x):
            if x == 0 or x == 1:
                return 1
            return x * fun(x-1)
        
        print(fun(n))
