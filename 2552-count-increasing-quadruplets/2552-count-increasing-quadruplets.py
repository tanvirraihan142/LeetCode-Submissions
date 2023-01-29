class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        l, r, s = [[0] * len(nums) for _ in range(len(nums) + 1)], [[0] * len(nums) for _ in range(len(nums) + 1)], 0
        for i in range(len(nums) - 1):
            for j in range(1, nums[i] + 1):
                l[j][i + 1] = l[j][i]
            for j in range(nums[i] + 1, len(nums) + 1):
                l[j][i + 1] = l[j][i] + 1
        for i in range(len(nums) - 1, 0, -1):
            for j in range(1, nums[i]):
                r[j][i - 1] = r[j][i] + 1
            for j in range(nums[i], len(nums) + 1):
                r[j][i - 1] = r[j][i]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s += l[nums[j]][i] * r[nums[i]][j] if nums[i] > nums[j] else 0
        return s