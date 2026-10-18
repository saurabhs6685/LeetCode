import math
from typing import List


class Solution:

  def numOfWays(self, nums: List[int]) -> int:
    MOD = 10**9 + 7

    def dfs(elements: List[int]) -> int:
      if len(elements) <= 2:
        return 1

      root = elements[0]
      left = [x for x in elements[1:] if x < root]
      right = [x for x in elements[1:] if x > root]

      # Ways to interleave left and right elements: comb(len(left) + len(right), len(left))
      interleave_ways = math.comb(len(left) + len(right), len(left))

      return (interleave_ways * dfs(left) * dfs(right)) % MOD

    # Subtract 1 to exclude the original array permutation itself
    return (dfs(nums) - 1) % MOD