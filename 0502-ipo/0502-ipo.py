class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        couple_list = list(zip(capital, profits))
        # couple_list.sort(key = lambda x: (x[0], -x[1]))
        couple_list.sort(reverse=True)
        max_heap = []
        ans = 0

        for i in range(k):
            while couple_list and couple_list[-1][0] <= w:
                cc, cp = couple_list.pop()
                heapq.heappush(max_heap, (-cp, cc))

            # if max_heap empty, then do what? 
            if not max_heap:
                break

            picked = heapq.heappop(max_heap)
            w = w - picked[0]
            ans -= picked[0]

        return w
        