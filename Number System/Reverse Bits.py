class Solution:
    def reverseBits(self, n: int) -> int:
        

        bits = ""
        while n > 0:
            rem = n % 2
            bits += str(rem)
            n //= 2
        rem = 32 - len(bits)
        rem = '0' * rem
        bits += rem
        print(bits)
        num = 0
        for i in range(len(bits)):
            num += ( int(bits[len(bits) - i - 1]) * 2 ** i)
        return num
