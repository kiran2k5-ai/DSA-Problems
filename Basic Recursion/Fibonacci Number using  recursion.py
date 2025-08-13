class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def fib_fun(n):

            if n == 1:
                return 1

            if n == 0:
                return 0
            
            return fib_fun(n-1)+fib_fun(n-2)
        
        return fib_fun(n)
