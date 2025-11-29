class Solution:
    def bitwiseComplement(self, n: int) -> int:

        if n == 0:
            return 1
        bits = ""
        while n > 0:
            bits += str(n % 2)
            n //= 2
        bits = list(bits)
        num = 0
        print(bits)
        for i in range(len(bits)):
            if bits[i] == '1': bits[i] = '0'
            elif bits[i] == '0': bits[i] = '1'
            num += (int(bits[i]) * 2**i)
        print(bits)
        return num
        

        
