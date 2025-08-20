class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst1 , lst2 , org = [] , [] , []
        for i in range(len(nums)):
            if nums[i] > 0:
                lst1.append(nums[i])
            else:
                lst2.append(nums[i])
        for j in range(len(lst1)):
            org.extend([lst1[j],lst2[j]])
        return org
