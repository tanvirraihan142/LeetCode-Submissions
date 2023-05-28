class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num_int = int(num)
        num_str = str(num_int).rstrip('0')
        return num_str