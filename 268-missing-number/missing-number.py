class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        # Sum of first n natural numbers: n * (n + 1) // 2
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum