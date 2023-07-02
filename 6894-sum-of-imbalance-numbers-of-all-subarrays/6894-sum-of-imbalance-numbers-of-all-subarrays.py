class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            tmp = [0] * (n + 1)
            tmp[nums[i]] = 1
            cnt = 0
            for j in range(i + 1, n):
                if tmp[nums[j]] == 0:
                    cnt += 1
                    if nums[j] > 0 and tmp[nums[j] - 1] == 1: cnt -= 1
                    if nums[j] < n and tmp[nums[j] + 1] == 1: cnt -= 1
                    tmp[nums[j]] = 1
                ans += cnt
        return ans