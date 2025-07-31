class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def hp(s):
            if s==s[0]*len(s):
                return (s[0],len(s))
            for i in range(2,len(s)+1):
                if not len(s)%i:
                    if s[:i]*(len(s)//i)==s:
                        return (s[:i],len(s)//i)       
        def HCF(a,b):
            if a>b:
                b,a=a,b
            if not b%a:
                return a   
            return HCF(a,b%a)                    
        if len(str1)>len(str2):
            str1,str2=str2,str1
        if str1 not in str2:
            return ""    
        (bb1,n1)=hp(str1)
        (bb2,n2)=hp(str2) 
        if bb1!=bb2:
            print(str1,bb1,bb2)
            return ""    
        GCD=HCF(n1,n2)    
        return bb1*GCD 