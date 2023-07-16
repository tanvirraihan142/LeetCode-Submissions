class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        sett = set(forbidden)
        left = 0
        n = len(word)
        maxx = 0
        for right in range(n):
            while left <= right:
                flag = True
                for length in range(1, 11):
                    st = right - length + 1
                    if st < left:
                        break
                    if word[st: right + 1] in sett:
                        left = st + 1
                        flag = False
                        break
                if flag: 
                    break
            maxx = max(maxx, right - left + 1)
        return maxx