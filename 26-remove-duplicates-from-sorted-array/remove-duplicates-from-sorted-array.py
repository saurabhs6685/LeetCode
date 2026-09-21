class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        k = 1
        for x in nums[1:]:
            if x != nums[k - 1]:
                nums[k] = x
                k += 1
                
        return k