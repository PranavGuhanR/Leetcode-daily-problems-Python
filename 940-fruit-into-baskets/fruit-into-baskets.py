class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        f=[0,0]
        s=[0,0]
        l=ma=1
        for i in range(1,len(fruits)):
            if fruits[i] not in [fruits[f[0]],fruits[s[0]]]:
                ma=max(ma,l) 
                if s[1]>f[1]:
                    s[0]=f[1]+1
                    f=[s[0],s[1]]
                elif s[1]<f[1]:
                    f[0]=s[1]+1  
                s=[i,i]  
                l=i-f[0]+1
            else:
                l+=1
                if fruits[i]==fruits[f[0]]:
                    f[1]=i
                if fruits[i]==fruits[s[0]]:
                    s[1]=i        
        ma=max(ma,l)       
        return ma         