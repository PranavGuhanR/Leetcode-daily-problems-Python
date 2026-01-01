class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=1
        for i in range(len(digits)-1,-1,-1):
            (c,digits[i])=((digits[i]+c)//10,(digits[i]+c)%10)   
        if c:
            return ([1]+digits)
        return digits   