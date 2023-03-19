class WordDictionary:

    def __init__(self):
        self.root = dict()
        
    def addWord(self, word: str) -> None:
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, dict())
        current_dict["_end_"] = True

    def search(self, word: str) -> bool:
        current_dict = self.root
        alphabets = [chr(i+97) for i in range(26)]
        found = False
        
        def dfs(node, idx, res):
            nonlocal found
            if idx==len(word):
                if "_end_" in node:
                    found = True
                return
            c = word[idx]
            if c == ".":
                for a in alphabets:
                    if a in node:
                        dfs(node[a], idx+1, res+a)
            else:
                if c in node:
                    dfs(node[c],idx+1, res+c)
                                
        dfs(current_dict, 0,"")
        return found
        
