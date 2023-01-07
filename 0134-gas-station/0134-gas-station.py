class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, cur = 0, 0
        length, start = len(gas), 0
        
        for i, (g, c) in enumerate(zip(gas, cost)):
            diff = g - c
            total += diff
            cur += diff
            if cur < 0:
                start = i + 1
                cur = 0
            
        return -1 if total < 0 else start