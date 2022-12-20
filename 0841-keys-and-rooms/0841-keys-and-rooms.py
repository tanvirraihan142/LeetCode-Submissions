class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        
        while stack:
            u = stack.pop()
            for v in rooms[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)
                    
        return all(seen)