# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        l, r = [], []
        def d(n):
            if n:
                d(n.left)
                l.append(n.val)
                d(n.right)
        d(root)
        for n in queries:
            r.append([l[bisect_right(l, n) - 1] if bisect_right(l, n) > 0 else -1, l[bisect_left(l, n)] if bisect_left(l, n) < len(l) else -1])
        return r