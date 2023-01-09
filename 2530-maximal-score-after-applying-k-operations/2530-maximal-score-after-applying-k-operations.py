class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
    
        for num in nums:
            heapq.heappush(heap, (-num, num))

        score = 0
        for i in range(k):
            max_num, num = heapq.heappop(heap)
            score += num
            new_num = math.ceil(num /3)
            heapq.heappush(heap, (-new_num, new_num))

        return score