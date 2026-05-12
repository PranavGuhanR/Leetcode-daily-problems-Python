class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: (-(x[1]-x[0]),-x[0]))

        def ok(n):

            for i in range(len(tasks)):
                if n>=tasks[i][1]:
                    n-=tasks[i][0]
                else:
                    return -1

            return 1

        lb=ub=0
        for i in range(len(tasks)):
            lb+=tasks[i][0]
            ub+=tasks[i][1]

        ans=ub

        while lb<=ub:
            m=(lb+ub)//2
            if ok(m)==1:
                ub=m-1
                ans=m
            else:
                lb=m+1

        return ans        