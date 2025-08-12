class Solution:
    def countDigit(self, n):

        count=len(str(n))
        if count == 1:
            print("There are",count,"digits in ",n)
        else:
            print("There is only",count,"digits in ",n)
