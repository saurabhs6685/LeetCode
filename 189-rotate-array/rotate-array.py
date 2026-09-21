class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # 1. Reverse whole list
        reverse(0, n - 1)
        # 2. Reverse first k elements
        reverse(0, k - 1)
        # 3. Reverse the rest
        reverse(k, n - 1)