class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        greater_numbers=0
        smaller_numbers=0
        for i in nums:
            if i>target:
                greater_numbers+=1
            elif i<target:
                smaller_numbers+=1
                
        return [i for i in range(smaller_numbers,len(nums)-greater_numbers)]            