# Last updated: 4/23/2025, 5:41:42 PM
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = defaultdict(int)  # dp[rem] = count of subarrays ending at prev index with product % k == rem
    
        for num in nums:
            new_dp = defaultdict(int)
    
            num_mod = num % k
            new_dp[num_mod] += 1
            result[num_mod] += 1
    
            for rem in dp:
                new_rem = (rem * num_mod) % k
                new_dp[new_rem] += dp[rem]
                result[new_rem] += dp[rem]
    
            dp = new_dp
    
        return result