
from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        count = [0] * 31

        for num in nums:
            for bit in range(31):
                if (num >> bit) & 1:
                    count[bit] += 1

        ans = 0

        for _ in range(k):
            num = 0

            for bit in range(31):
                if count[bit] > 0:
                    num |= (1 << bit)
                    count[bit] -= 1

            ans = (ans + num * num) % mod

        return ans
