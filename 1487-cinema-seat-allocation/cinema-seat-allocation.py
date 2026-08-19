class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        crgc=0
        reservedSeats.sort()
        lr=reservedSeats[0][0]
        cr=r1=r2=r3=1
        for i in range(len(reservedSeats)):
            if lr<reservedSeats[i][0]:
                lr=reservedSeats[i][0]
                cr+=1
                crgc+=max(r1,r2+r3)
                r1=r2=r3=1
            if 4<=reservedSeats[i][1]<=7:
                r1*=0
            if 2<=reservedSeats[i][1]<=5:
                r2*=0
            if 6<=reservedSeats[i][1]<=9:
                r3*=0
        ncr=n-cr
        crgc+=max(r1,r2+r3)    
        return crgc+ncr*2  