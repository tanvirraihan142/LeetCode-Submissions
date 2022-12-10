class Solution:
    def maxJump(self, stones: List[int]) -> int:
        ans = stones[1] - stones[0]
        for i in range(2, len(stones)):
            res = stones[i] - stones[i-2]
            ans = max(ans, res)
        return ans