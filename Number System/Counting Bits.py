class Solution:
    def countBits(self, n: int) -> List[int]:
        
        lst = []
        for i in range(n+1):
            count = 0   
            num = 2 ** i
            bits = bin(i)
            for i in range(len(bits)):
                if bits[i] == '1':
                    count +=1
            lst.append(count)

        return lst
