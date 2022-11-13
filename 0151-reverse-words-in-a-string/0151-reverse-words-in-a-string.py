class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        reverse_words = []
        for i in range(len(words)-1,-1,-1):
            if len(words[i])>0:
                reverse_words.append(words[i])
        return " ".join(reverse_words)