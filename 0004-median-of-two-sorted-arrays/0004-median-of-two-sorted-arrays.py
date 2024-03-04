class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N1, N2 = len(nums1), len(nums2)
        
        # Make sure nums2 is the shorter one.
        if N1 < N2: 
            nums1, N1, nums2, N2 = nums2, N2, nums1, N1
            
        l, r = 0, N2*2
        
        while l <= r:
            # Try Cut 2 
            j = (l + r) >> 1
            # Calculate Cut 1 accordingly
            i = N1 + N2 - j
            
            # Get L1, R1, L2, R2 respectively
            L1 = float('-inf') if i == 0 else nums1[(i-1)>>1]
            L2 = float('-inf') if j == 0 else nums2[(j-1)>>1]
            R1 = float('inf') if i == 2*N1 else nums1[i>>1]
            R2 = float('inf') if j == 2*N2 else nums2[j>>1]
            
            # nums1's lower half is too big; need to move mid1 left (mid2 right)
            if L1 > R2: l = j + 1
                
            # nums2's lower half is too big; need to move mid2 left
            elif L2 > R1: r = j - 1
            else:
                return (max(L1, L2) + min(R1, R2))/2.0
        return -1