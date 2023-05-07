class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res = []
        for i, v in enumerate(nums):
            set1 = set(nums[:i+1])
            set2 = set(nums[i+1:])
            res.append(len(set1)-len(set2))
        return res