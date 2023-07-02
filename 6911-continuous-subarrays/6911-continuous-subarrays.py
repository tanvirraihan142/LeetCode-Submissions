class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        cnt = Counter()
        ans = 0
        while l < n:
            while r < n and (len(cnt) == 0 or (nums[r] - min(cnt) <= 2 and max(cnt) - nums[r] <= 2)):
                cnt[nums[r]] += 1
                r += 1
            ans += r - l
            cnt[nums[l]] -= 1
            if cnt[nums[l]] == 0: del cnt[nums[l]]
            l += 1
        return ans