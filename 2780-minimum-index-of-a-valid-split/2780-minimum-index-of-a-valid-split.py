class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)

        vmax = -1
        dominant = -1
        _count = collections.Counter(nums)
        for k,v in _count.items():
          if v > vmax:
            vmax = v
            dominant = k

        c = 0
        left_count = 0 
        for i in range(len(nums)):
          v = nums[i]
          if v == dominant:
              left_count += 1
          if left_count * 2 > (i+1) and (_count[dominant] - left_count)*2 > (n-1-i):
            return i

        return -1