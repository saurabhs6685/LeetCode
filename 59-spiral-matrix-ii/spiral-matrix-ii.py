class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        a = [[0]*n for _ in range(n)]
        t, b , l, r, x = 0, n-1, 0, n-1, 1

        while t <= b and l <= r:
            for j in range(l, r+1):
                a[t][j] = x
                x += 1
            t += 1

            for i in range(t, b+1):
                a[i][r] = x
                x += 1
            r -= 1

            if t <= b:
                for j in range(r, l-1, -1):
                    a[b][j] = x
                    x += 1
                b -= 1

            if l <=r:
                for i in range(b, t-1, -1):
                    a[i][l] = x
                    x += 1
                l += 1

        return a