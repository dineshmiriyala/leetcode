"""Boiler plate code can be found in leetcode"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i,j in enumerate(nums):
            if target - j in dict:
                return [dict[target - j],i]
            else:
                dict[j] = i
        return
    


