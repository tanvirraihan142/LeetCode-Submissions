class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary = bin(n)[2:][::-1]  # convert to binary string, remove '0b' prefix
        even_count = 0
        odd_count = 0
        # print(binary)

        for i in range(len(binary)):
            
          if i%2 == 0 and binary[i]=='1':
            even_count += 1
            
          elif i%2 == 1 and binary[i]=='1':
            odd_count += 1
            
        return [even_count, odd_count]