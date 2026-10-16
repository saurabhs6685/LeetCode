
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        square = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                length = end - start + 1
                d = 1

                square[node] = (
                    square[node] + 2 * total[node] * d
                    + length * d * d
                )
                total[node] += length * d
                lazy[node] += d
                return

            mid = (start + end) // 2
            lc = 2 * node
            rc = lc + 1

            if lazy[node]:
                d = lazy[node]

                for child, l, r in (
                    (lc, start, mid),
                    (rc, mid + 1, end)
                ):
                    length = r - l + 1
                    square[child] += (
                        2 * d * total[child] + length * d * d
                    )
                    total[child] += length * d
                    lazy[child] += d

                lazy[node] = 0

            if left <= mid:
                update(lc, start, mid, left, right)

            if right > mid:
                update(rc, mid + 1, end, left, right)

            total[node] = total[lc] + total[rc]
            square[node] = square[lc] + square[rc]

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1

            update(1, 0, n - 1, left, i)

            ans = (ans + square[1]) % MOD
            last[x] = i

        return ans
