class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if (len(nums)==1):
            return True
        
        queue = deque([0])
        visited = set()
        visited.add(0)

        while len(queue)>0:
            node = queue.pop()

            if (nums[node]==0):
                continue

            for i in range(1,nums[node]+1):
                if node+i not in visited and node+i < len(nums)-1:
                    queue.append(node+i)
                    visited.add(node+i)
                elif node+i == len(nums)-1:
                    return True
                
        return False