class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1.0 / x
        res = 1.0
        cnt = 0
        while n:
            t = x
            if n % 2:
                for i in range(cnt):
                    t = t * t
                res *= t
            cnt += 1
            n = n // 2
        return res