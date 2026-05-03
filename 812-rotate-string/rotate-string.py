class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)==1:
            return s==goal
        if s==goal:
            return True    
        for i in range(1,len(s)):
            cs=s[i::]+s[0:i]  
            if cs==goal:
                return True
        return False             