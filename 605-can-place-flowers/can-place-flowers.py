class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans=0
        s=flowerbed[0]
        c=(flowerbed[0]+1)%2
        e=0
        for i in range(1,len(flowerbed)):
            if flowerbed[i]:
                e=1
                if c-s-e>0:
                    ans+=(c-s-e+1)//2
                s=1
                e=0
                c=0
            else:
                c+=1
        if not flowerbed[-1]:
            ans+=(c-s+1)//2        
        return ans>=n