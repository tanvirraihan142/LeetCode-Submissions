class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        b = []
        
        for i in s:
            if i not in b:
                b.append(i)
                if len(b)>l:
                    l = len(b)
            else:
                if len(b)>l:
                    l = len(b)
                b = b[b.index(i)+1:]
                b.append(i)
            print(b)
        return l