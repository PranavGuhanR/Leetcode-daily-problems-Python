class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        def mg(L):
            g=abs(L[0]-L[1])+abs(L[1]-L[2])+abs(L[2]-L[0])
            if len(L)==3:
                return g

            MG=g

            for i in range(3,len(L)):
                g-=abs(L[i-3]-L[i-2])+abs(L[i-1]-L[i-3])    
                g+=abs(L[i]-L[i-2])+abs(L[i-1]-L[i])   
                MG=min(MG,g)

            return MG

        d={}

        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)       
            else:
                d[nums[i]]=[i]

        ans=10**6

        for i in d.keys():
            if len(d[i])>=3:
                ans=min(ans,mg(d[i]))   

        if ans==10**6:
            return -1

        return ans            
