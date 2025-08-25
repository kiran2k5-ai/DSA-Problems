class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = {}
        for i in range(len(nums)):
            if nums[i] not in res:
                res[nums[i]] = 1
            else:
                res[nums[i]] += 1
        n=len(nums)
        k = n//3
        lst = []
        for key in res:
            if res[key] > k:
                lst.append(key)
        return lst
