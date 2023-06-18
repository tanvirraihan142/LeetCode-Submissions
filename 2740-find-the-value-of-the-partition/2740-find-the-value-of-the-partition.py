class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        minDist = 10**10
        
        for i in range(len(nums)-1):
            minDist = min(minDist, nums[i+1] - nums[i])

        return minDist