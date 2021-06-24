class Solution:
    def cuttingRope(self, n: int) -> int:
        res = 1
        for i in range(2, n):
            t1 = n // i
            t2 = n % i
            num = 1
            for j in range(i):
                if t2:
                    num *= t1 + 1
                    t2 -= 1
                else:
                    num *= t1
            res = num if num > res else res
        return res