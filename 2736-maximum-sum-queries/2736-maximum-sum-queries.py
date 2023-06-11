class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        vs = []
        for i in range(n): vs.append((nums1[i], nums2[i]))
        vs.sort()
        ys = sorted(list(set(nums2)))
        nn = len(ys)
        mx=1
        while mx<=nn: mx<<=1
        ix = [-1]*(mx+mx)
        m = len(queries)
        r = [-1]*m
        tq = []

        for i in range(m):
            tq.append((queries[i][0], queries[i][1], i))
        tq.sort(reverse=True)
        j = n-1
        def setv(s, v):
            s+=mx
            ix[s]=max(ix[s], v)
            s>>=1
            while s:
                ix[s]=max(ix[s*2], ix[s*2+1])
                s>>=1
        def findm(s):
            e=mx+mx-1
            s+=mx
            r = -1
            while s<=e:
                if s&1:
                    r=max(r, ix[s])
                    s+=1
                if (e&1)==0:
                    r=max(r, ix[e])
                    e-=1
                s>>=1
                e>>=1
            return r
            
        for x, y, i in tq:
            while j>=0 and vs[j][0]>=x:
                k = bisect_left(ys, vs[j][1])
                setv(k, vs[j][1]+vs[j][0])
                j-=1
            k = bisect_left(ys, y)
            r[i] = findm(k)
        return r