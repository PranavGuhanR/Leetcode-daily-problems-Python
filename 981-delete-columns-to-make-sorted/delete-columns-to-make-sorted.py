class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c=0
        for i in range(len(strs[0])):
            s='a'
            for j in range(len(strs)):
                if s>strs[j][i]:
                    c+=1
                    break
                else:
                    s=strs[j][i]
        return c            