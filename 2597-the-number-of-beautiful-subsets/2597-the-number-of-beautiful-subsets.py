class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        total = 0
        
        def checkSet(cur, i):
            nonlocal total
            
            if not cur:
                total += 1
                cur.add(nums[i])
                
            elif nums[i] + k not in cur and nums[i] - k not in cur:
                total += 1
                newSet = cur.copy()
                if i < len(nums)-1:
                    checkSet(newSet, i + 1)
                cur.add(nums[i])
            if i < len(nums)-1:
                checkSet(cur, i + 1)
 
        for i in range(len(nums)):
            checkSet(set(), i)
 
        return total