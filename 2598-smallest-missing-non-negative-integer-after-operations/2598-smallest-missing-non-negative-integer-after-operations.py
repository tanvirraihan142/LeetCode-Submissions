class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        if value == 1:
            return len(nums)
        
        for i in range(len(nums)):
            nums[i] = nums[i]%value
        
        count = Counter(nums)
        missing = 0
        
        while True:
            x = missing%value
            if x not in count:
                return missing
            elif count[x] <= 0:
                return missing
            else:
                count[x] -= 1
            missing += 1
