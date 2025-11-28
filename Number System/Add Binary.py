class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if a == '0' and b == '0':
            return '0'
        num_a = 0
        num_b = 0
        for i in range(len(a)):
            num_a += (int(a[len(a)-i-1]) * 2**i)
        for i in range(len(b)):
            num_b += (int(b[len(b)-i-1]) * 2**i)

        num_a += num_b
        bin_num = ''
        while num_a > 0:
            bin_num += str(num_a % 2)
            num_a //= 2
        return bin_num[::-1]
