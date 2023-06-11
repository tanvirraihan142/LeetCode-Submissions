class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        a = nums1
        b = nums2
        q = queries
        n = len(a)
        m = len(q)
        r = [-1] * m
        a_ord = sorted(range(n), key=a.__getitem__)
        q_ord = sorted(range(m), key=q.__getitem__)
        a_ord_idx = n - 1
        b_val = set(b)
        b_val.update(set(y for x, y in q))
        b_val = sorted(b_val, reverse=True)
        b_pos = {v: i for i, v in enumerate(b_val)}
        fen_sz = len(b_pos)
        fen = [-1] * (fen_sz + 1)
        
        def _get(i):
            r = -1
            while i > 0:
                r = max(r, fen[i])
                i -= i & -i
            return r
        
        def _upd(i, v):
            i += 1
            while i <= fen_sz:
                fen[i] = max(fen[i], v)
                i += i & -i
                
        for q_idx in reversed(q_ord):
            x, y = q[q_idx]
            while a_ord_idx >= 0 and a[a_ord[a_ord_idx]] >= x:
                idx = a_ord[a_ord_idx]
                fen_idx = b_pos[b[idx]]
                _upd(fen_idx, a[idx] + b[idx])
                a_ord_idx -= 1
            r[q_idx] = _get(b_pos[y] + 1)
        return r