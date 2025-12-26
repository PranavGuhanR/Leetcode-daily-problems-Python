class Solution:
    def bestClosingTime(self, customers: str) -> int:
        l=[0]*(len(customers)+1)
        for i in range(len(l)-2,-1,-1):
            l[i]=l[i+1]
            if customers[i]=='Y':
                l[i]+=1
        op=0  
        s=len(customers) 
        ans=0     
        for i in range(len(l)-1):
            if op+l[i]<s:
                s=op+l[i]
                ans=i
            if customers[i]=='N':
                op+=1
        if op+l[len(l)-1]<s:
                ans=len(l)-1       
        return ans        