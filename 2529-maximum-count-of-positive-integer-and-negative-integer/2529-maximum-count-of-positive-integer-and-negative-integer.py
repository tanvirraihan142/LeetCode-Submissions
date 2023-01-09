class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos_cnt = 0
        neg_cnt = 0
        for i,v in enumerate(nums):
            if v > 0:
                pos_cnt += 1
            elif v < 0:
                neg_cnt += 1
        return max(pos_cnt, neg_cnt)