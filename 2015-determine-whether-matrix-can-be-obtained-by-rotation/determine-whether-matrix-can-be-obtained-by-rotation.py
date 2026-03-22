class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def ok180():
            for i in range(len(mat)):
                for j in range(len(mat)):
                    if  not(target[len(mat)-1-i][len(mat)-1-j]==mat[i][j]):
                        return False
            return True            

        def ok90():
            for i in range(len(mat)):
                for j in range(len(mat)):
                    if not(target[j][len(mat)-1-i]==mat[i][j]):
                        return False
            return True 

        def ok270():
            for i in range(len(mat)):
                for j in range(len(mat)):
                    if not(target[len(mat)-1-j][i]==mat[i][j]):
                        return False
            return True 

        def ok0():
            for i in range(len(mat)):
                for j in range(len(mat)):
                    if not(target[i][j]==mat[i][j]):
                        return False
            return True 
            
        
        return ok0() or ok90() or ok180() or ok270()