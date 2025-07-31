class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        sb=set([arr[0]])
        pb=set([arr[0]])
        cb=set()
        for i in range(1,len(arr)):
            cb.add(arr[i])
            pb.add(arr[i])
            for j in pb:
                sb.add(j|arr[i])
                cb.add(j|arr[i])
            pb=cb
            cb=set()
        return len(sb)        