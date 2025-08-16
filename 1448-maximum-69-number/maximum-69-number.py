class Solution:
    def maximum69Number (self, num: int) -> int:
        n=num
        for i in range(len(str(num))):
            if str(num)[i]=='6':
                return  num + 3*(10**(len(str(num))-1-i)) 
        return num        
