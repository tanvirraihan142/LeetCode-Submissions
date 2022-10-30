# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        Depth, Height = collections.defaultdict(int), collections.defaultdict(int)
        
        def dfs(node, depth):
            if not node:
                return -1
            
            Depth[node.val] = depth
            
            #height for the current node
            cur = max(dfs(node.left, depth+1), dfs(node.right, depth+1)) + 1
            Height[node.val] = cur
            return cur
        dfs(root, 0)
        #cousins are nodes that are in the same depth
        cousins = {}
        for val, depth in Depth.items():
            if depth not in cousins:
                cousins[depth] = []
            heapq.heappush(cousins[depth], (-Height[val], val))
            
            
        ans = []
        for q in queries:
            
            #looking at the cousins of the same depth as the query node q
            depth = Depth[q]
            # print(q, depth)
            if len(cousins[depth]) == 1:
                ans.append(depth-1)
            elif cousins[depth][0][1] == q:
                tmp = heapq.heappop(cousins[depth])
                ans.append(-cousins[depth][0][0] + depth)
                heapq.heappush(cousins[depth], tmp)
            else:
                ans.append(-cousins[depth][0][0] + depth)
        
        return ans