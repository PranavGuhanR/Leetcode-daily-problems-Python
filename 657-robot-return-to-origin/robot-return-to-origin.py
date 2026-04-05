class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves=Counter(moves)
        if moves['L']==moves['R']:
            if moves['U']==moves['D']:
                return True
        return False        