class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = 0
        result = 0
        even_count = 0

        for left in range(n):
          right = left
          if (nums[left] %2 == 0) and (nums[left] <= threshold):
            while  (right < len(nums)-1) and (nums[right+1] <= threshold) and (nums[right] %2 != nums[right+1]%2):
              right += 1
              # print(left, right, nums[left:right+1])
            result = max(result, right - left + 1)

        return result