
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        k = (n + 1) // 2

        small = nums[:n - k]
        large = nums[n - k:]

        result = 0

        for num in large:
            result += num * num

        for num in small:
            result -= num * num

        return result
