class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        en=n//2
        on=en+n%2
        em=m//2
        om=em+m%2
        return en*om+em*on