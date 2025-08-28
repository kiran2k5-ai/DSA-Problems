from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # initialize
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]

        # iterate through array
        for i in range(1, len(nums)):
            n = nums[i]
            # if n is negative, swap max and min
            if n < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            
            # update max and min
            max_so_far = max(n, max_so_far * n)
            min_so_far = min(n, min_so_far * n)

            # update result
            result = max(result, max_so_far)

        return result
