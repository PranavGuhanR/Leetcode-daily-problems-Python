class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mi=10**7
        l=[]
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[j]-arr[i]<mi:
                    mi=arr[j]-arr[i]
                    l=[[arr[i],arr[j]]]
                elif arr[j]-arr[i]==mi:
                    l.append([arr[i],arr[j]]) 
                else:
                    break
        return l                  