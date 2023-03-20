class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        
        if len(flowerbed)==1:
            if flowerbed[0] == 0:
                flowerbed[0] = 1
                count += 1
        else:
            for i in range(0, len(flowerbed)):
                if i==0:
                    if flowerbed[i] == flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        count += 1

                elif i==len(flowerbed)-1:
                    if flowerbed[i] == flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        count += 1
                else:
                    if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        count += 1
        # print(count)
        return count >= n