class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s=set()
        for i in range(len(arr1)):
            for j in range(len(str(arr1[i]))):
                if str(arr1[i])[:j+1] not in s:
                    s.add(str(arr1[i])[:j+1])
        m=0  
        for i in range(len(arr2)):
            for j in range(len(str(arr2[i]))):
                if str(arr2[i])[:j+1] not in s:
                    break
                else:
                    m=max(m,j+1)
        return m                                  