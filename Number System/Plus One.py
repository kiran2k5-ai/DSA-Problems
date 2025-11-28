class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        lst = []
        for i in range(len(digits)):
            lst.append(str(digits[i]))
        lst = ''.join(lst)
        lst = int(lst)
        lst += 1
        new_lst = []
        lst = list(str(lst))
        for i in range(len(lst)):
            new_lst.append(int(lst[i]))
        return new_lst
