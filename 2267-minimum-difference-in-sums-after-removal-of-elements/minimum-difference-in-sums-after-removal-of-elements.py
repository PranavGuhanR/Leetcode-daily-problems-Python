import heapq
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        p1= [0] * (n + 1)           #p1[i]- minimum sum possible
                                    #out of any n element from the 
                                    #array nums[0:n+i] 
        one = [-i for i in nums[:n]]
        heapq.heapify(one)
        p1[0] = -sum(one)
        for i in range(n, 2*n):
            if -nums[i] > one[0]:
                out = -heapq.heappop(one)
                p1[i - n + 1] = p1[i - n] + nums[i] - out
                heapq.heappush(one, -nums[i])
            else:
                p1[i - n + 1] = p1[i - n]
        
        two = nums[2 * n:]
        heapq.heapify(two)
        sum_two = sum(two)
        res = p1[-1] - sum_two
        for i in range(2 * n - 1, n - 1, -1):
            if nums[i] > two[0]:
                out = heapq.heappop(two)
                sum_two += nums[i] - out
                heapq.heappush(two, nums[i])
            res = min(res, p1[i - n] - sum_two)  
        return res