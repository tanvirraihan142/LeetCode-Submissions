class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        max_pos = max(forbidden + [x]) + a
        
        # create a set of forbidden positions for faster lookup
        forbidden_set = set(forbidden)

        # initialize the visited set to keep track of visited positions and jumps
        visited = set()
        visited.add((0, False))  # starting position at 0 with no backward jump

        # initialize a queue for BFS
        queue = deque([(0, False, 0)])

        # BFS to find the minimum number of jumps needed to reach x
        while queue:
            curr_pos, curr_jump_backward, jumps = queue.popleft()
            if curr_pos == x:
                return jumps
            
            if curr_pos + a not in forbidden_set and (curr_pos + a, False) not in visited and curr_pos + a <= 5999:
                visited.add((curr_pos + a, False))
                queue.append((curr_pos + a, False, jumps + 1))
                
            if curr_pos - b > 0 and not curr_jump_backward and curr_pos - b not in forbidden_set and (curr_pos - b, True) not in visited:
                visited.add((curr_pos - b, True))
                queue.append((curr_pos - b, True, jumps + 1))
                
        return -1