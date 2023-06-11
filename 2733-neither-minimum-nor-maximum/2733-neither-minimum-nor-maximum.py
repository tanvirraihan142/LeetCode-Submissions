class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)==1 or len(nums)==2:
            return -1
        
        nums.sort()
        if nums[1] != nums[0]:
            return nums[1]