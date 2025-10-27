class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        c=0
        p=sum([int(j) for j in bank[0]])
        for i in range(1,len(bank)):
            s=sum([int(j) for j in bank[i]])
            if s:
                c+=p*s
                p=s
        return c             