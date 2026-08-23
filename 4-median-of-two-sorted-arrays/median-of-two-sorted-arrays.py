class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Hamesha smaller array par binary search karenge for O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2

        low = 0
        high = m

        while low <= high:
            i = (low + high) // 2  # Partition in nums1
            j = total_left - i     # Partition in nums2

            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')

            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            # Correct partition condition
            if left1 <= right2 and left2 <= right1:
                # Odd length case
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                # Even length case
                return (max(left1, left2) + min(right1, right2)) / 2.0
            
            elif left1 > right2:
                # nums1 se left side zyada bada element le liya, peeche jao
                high = i - 1
            else:
                # nums1 ka right side chota reh gaya, aage badho
                low = i + 1

        return 0.0