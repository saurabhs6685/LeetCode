import heapq

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        # Top 3 largest aur top 2 smallest numbers nikal lo
        largest = heapq.nlargest(3, nums)
        smallest = heapq.nsmallest(2, nums)
        
        # Product calculate karke max return karo
        return max(largest[0] * largest[1] * largest[2], smallest[0] * smallest[1] * largest[0])