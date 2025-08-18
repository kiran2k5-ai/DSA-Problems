class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_maj = {}
        for i in range(len(nums)):
            if nums[i] not in dict_maj:
                dict_maj[nums[i]] = 1
            else:
                dict_maj[nums[i]] += 1
        return max(dict_maj, key=dict_maj.get) 
        
