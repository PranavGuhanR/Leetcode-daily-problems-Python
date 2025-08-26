class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        m=l=0
        for i in range(len(dimensions)):
            if (dimensions[i][0]**2+dimensions[i][1]**2)>l:
                m=dimensions[i][0]*dimensions[i][1]
                l=(dimensions[i][0]**2+dimensions[i][1]**2)
            elif (dimensions[i][0]**2+dimensions[i][1]**2)==l:
                if m<dimensions[i][0]*dimensions[i][1]:
                    m=dimensions[i][0]*dimensions[i][1]  
        return m             