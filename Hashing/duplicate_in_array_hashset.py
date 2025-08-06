#Find All Duplicates in an Array


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        res = []

        for i in range(len(nums)):
            n = abs(nums[i])
            if nums[n-1] < 0:
                res.append(n)
            else:
                nums[n-1]=-nums[n-1]

        return res
        
