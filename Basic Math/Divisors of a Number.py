class Solution:
    def divisors(self, n):

        l=[]
        for i in range(1,n):
            if n % i == 0:
                l.append(i)
        print(l)
