class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        Q = deque([(i, x) for i, x in enumerate(tickets)])
        # print(Q)
        time = 0
        
        while Q:
            i, x = Q.popleft()
            time += 1
            if x > 1:
                Q.append((i, x - 1))
            elif i == k:
                break
        
        return time