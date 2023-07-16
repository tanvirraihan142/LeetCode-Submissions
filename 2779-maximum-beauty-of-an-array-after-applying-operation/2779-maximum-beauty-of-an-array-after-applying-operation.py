class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_beauty = 0
        left = 0
        for right, num in enumerate(nums):
            while num - nums[left] > 2*k:
                left += 1
            max_beauty = max(max_beauty, right - left + 1)
 
        return max_beauty