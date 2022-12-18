class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words2 = [list(set(i)) for i in words]
        for i in range(len(words2)):
            words2[i].sort()
            words2[i] = str(words2[i])
        
        c = 0
        for i in range(len(words2)):
            for j in range(i+1, len(words2)):
                if words2[i] == words2[j]:
                    c += 1
                    
        return c