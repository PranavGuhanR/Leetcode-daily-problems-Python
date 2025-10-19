class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        s = list(map(int, s))
        n = len(s)
        step = gcd(b, n)
        g = gcd(a, 10)
        ans = [10]

        def modify(start: int) -> None:
            ch = t[start]  
            inc = ch % g - ch
            if inc:
                for j in range(start, n, 2):
                    t[j] = (t[j] + inc) % 10

        for i in range(0, n, step):      
            t = s[i:] + s[:i]
            modify(1)  
            if step % 2: 
                modify(0) 
            ans = min(ans, t)

        return ''.join(map(str, ans))