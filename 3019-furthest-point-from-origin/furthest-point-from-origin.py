class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        C=Counter(moves)
        return max(C['L'],C['R'])+C['_']-min(C['L'],C['R'])