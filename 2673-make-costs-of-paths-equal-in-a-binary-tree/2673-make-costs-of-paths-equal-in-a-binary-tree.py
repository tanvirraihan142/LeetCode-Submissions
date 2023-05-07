class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        result = 0
        
        while len(cost) > 1:
            x = cost.pop()
            y = cost.pop()
            result += abs(x-y)
            cost[len(cost)//2] += max(x, y)
        
        return result