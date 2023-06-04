class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        operations = 0
        
        if nums[0] == 1 and nums[-1] == len(nums):
            return 0
        
        _map = {}
        for i,v in enumerate(nums):
            _map[v] = i+1
        
        
        print(_map)
        result = 0
        
        if _map[1] != 1:
            result += _map[1] - 1
            
        if _map[len(nums)] != len(nums):
            result += len(nums) -_map[len(nums)] 
            
        if _map[len(nums)] < _map[1]:
            result -= 1
            
        return result