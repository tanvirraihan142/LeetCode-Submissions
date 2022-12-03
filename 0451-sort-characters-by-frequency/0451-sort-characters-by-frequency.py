class Solution:
    def frequencySort(self, s: str) -> str:
        _map = collections.Counter(s)
        _map = {k: v for k, v in sorted(_map.items(), reverse=True, key=lambda item: item[1])}
        
        s2 = ""
        for key in _map:
            s2 = s2 + key*_map[key]
            
        return s2