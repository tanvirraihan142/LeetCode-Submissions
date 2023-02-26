class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        
        for i in range(len(nums)-1):
            left_sum.append(left_sum[-1] + nums[i])
            
        # print(left_sum)
        right_sum = [0]
        
        for i in range(len(nums)-1,0,-1):
            right_sum.append(right_sum[-1] + nums[i])
            
        right_sum = right_sum[::-1]    
        # print(right_sum)
        
        ans = []
        for i in range(len(left_sum)):
            ans.append(abs(left_sum[i] - right_sum[i]))
            
        return ans