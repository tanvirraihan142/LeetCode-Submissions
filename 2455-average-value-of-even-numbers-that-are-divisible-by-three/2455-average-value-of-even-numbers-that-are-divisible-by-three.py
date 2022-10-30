class Solution:
    def averageValue(self, nums: List[int]) -> int:
        new_nums = []

        for i,v in enumerate(nums):
            if v%2==0 and v%3==0:
                new_nums.append(v)

        if not new_nums:
            return 0
        else:
            return floor(sum(new_nums)/len(new_nums))
