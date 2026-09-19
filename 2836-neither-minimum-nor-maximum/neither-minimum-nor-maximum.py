class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return -1
        
        # Taking just the first 3 elements guarantees finding a value 
        # that is neither the absolute minimum nor maximum of the entire array.
        sub = sorted(nums[:3])
        return sub[1]