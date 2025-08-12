class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > ((2**31)-1):
            return 0
        
        rev = 0
        if x > 0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
        while x != 0:
            num = x % 10
            rev = num + (10*rev)
            x = int(x//10)
        if rev > ((2**31)-1):
            return 0
        return rev * sign
