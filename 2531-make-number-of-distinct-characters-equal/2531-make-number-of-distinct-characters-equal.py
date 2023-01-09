class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        m1 = collections.Counter(word1)
        m2 = collections.Counter(word2)

        
        for i in range(26):
            for j in range(26):
                x = chr(i + ord('a'))
                y = chr(j + ord('a'))
                
                if x in m1 and m1[x]>0 and y in m2 and m2[y]>0:
                    m1[x] -= 1
                    m2[x] += 1
                    m1[y] += 1
                    m2[y] -= 1
                    
                    cnt1 = 0
                    cnt2 = 0
                    for k in range(26):
                        chctr = chr(k+ord('a'))
                        if chctr in m1 and m1[chctr]>0:
                            cnt1 += 1
                        if chctr in m2 and m2[chctr]>0:
                            cnt2 += 1
                    
                    if cnt1 == cnt2:
                        return True
                    
                    m1[x] += 1
                    m2[x] -= 1
                    m1[y] -= 1
                    m2[y] += 1
                    
        return False