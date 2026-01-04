l=[1]*(10**5+1)                             #sieve of eratosthenes
for i in range(2,int(10**2.5)+1):
    if l[i]==1:
        j=i*i
        while j<=10**5:
            l[j]=0
            j+=i
s=set() 
P=[]        
for i in range(2,len(l)):
    if l[i]:
        P.append(i)
        s.add(i)       
del l

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            j=0
            while (j<len(P)) and (P[j]<i):
                if i%P[j]==0:
                    sf=i//P[j]                                      #check for smalleest prime factor
                    if ((sf in s) and (sf!=P[j])) or sf==P[j]**2:   #divide the number by the prime
                        ans+=1+i+P[j]+sf                            #if the other factor is a different prime or square of the prime,
                    break                                           #then add all the factors
                j+=1  
        return ans          