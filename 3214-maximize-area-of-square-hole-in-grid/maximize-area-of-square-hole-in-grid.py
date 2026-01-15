class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        ccc=1       #current continuous count
        mcch=1       #maximum continuous count
        for i in range(1,len(hBars)):
            if hBars[i]==hBars[i-1]+1:
                ccc+=1
            else:
                mcch=max(ccc,mcch)
                ccc=1
        mcch=max(ccc,mcch)        
        ccc=1       #current continuous count
        mccv=1       #maximum continuous count
        for i in range(1,len(vBars)):
            if vBars[i]==vBars[i-1]+1:
                ccc+=1
            else:
                mccv=max(ccc,mccv)
                ccc=1
        mccv=max(ccc,mccv)
        return (min(mcch,mccv)+1)**2