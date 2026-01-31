class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans=letters[0]
        for i in letters:
            if i>target:
                if ans<=target:
                    return i
                return ans
        return ans        