from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lst = SortedList()    # maintain a sorted list
        
        res = []
        for i in range(len(nums)):
            lst.add(nums[i])            # O(logk)
            if len(lst) > k:
                lst.remove(nums[i-k])   # if we use heapq here, it will take O(k), but for sortedList, it takes O(logk)
            if len(lst) == k:
                median = lst[k//2] if k%2 == 1 else (lst[k//2-1] + lst[k//2]) / 2
                res.append(median)

        return res