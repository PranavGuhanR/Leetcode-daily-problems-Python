class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def solve(text: str, pattern: str, score: int):
            stack = []
            points = 0
                        #stack[-1]- previous character
                        #char- current character
            for char in text:
                if stack and stack[-1] == pattern[0] and char == pattern[1]:
                    stack.pop()
                    points += score
                else:
                    stack.append(char)
            return points, "".join(stack)
                    #First search for pattern with higher gain points
                    #Then, search for the least
        if x >= y:
            points1, remaining_s = solve(s, "ab", x)
            points2, _ = solve(remaining_s, "ba", y)
        else:
            points1, remaining_s = solve(s, "ba", y)
            points2, _ = solve(remaining_s, "ab", x)
            
        return points1 + points2