class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = set('AEIOUaeiou')
        s = list(s)
        i,j = 0, len(s)-1
        while i<j:
            while s[i] not in vowel and i<j:
                i = i + 1
            while s[j] not in vowel and i<j:
                j = j - 1
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
        return ''.join(s)