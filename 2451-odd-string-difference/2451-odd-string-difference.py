class Solution:
    def oddString(self, words: List[str]) -> str:
        difference = []
        _map = {}
        for j,word in enumerate(words):
            diff = []
            for i in range(1,len(word)):
                diff.append(ord(word[i]) - ord(word[i-1]))
            difference.append(tuple(diff))
            _map[tuple(diff)] = j

        _counter = collections.Counter(difference)
        for i,v in _counter.items():
            if v==1:
                return words[_map[i]]