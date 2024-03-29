class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0:
            return ""
        
        start, end = 0, 0
        
        def expandAroundCenter(s,left,right):
            L = left
            R = right
            
            while (L >= 0 and R < len(s) and s[L] == s[R]):
                L -= 1
                R += 1
                
            return R-L-1
        
        for i in range(len(s)):
            len1 = expandAroundCenter(s,i,i)
            len2 = expandAroundCenter(s,i,i+1)
            len_max = max(len1, len2)
            
            if len_max > (end-start):
                start = i - (len_max-1)//2
                end = i + len_max//2
                
        return s[start:end+1]