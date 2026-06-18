class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angh=(hour/12*360)%360+minutes/60*30
        angm=minutes/60*360    
        v=abs(angh-angm) 
        if v>180:
            return 360-v
        return v      