class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() == True:
            return True
        elif word.islower() == True:
            return True
        elif word[1:].islower() ==True  and word[:1].isupper()==True:
            return True
        else:
            return False