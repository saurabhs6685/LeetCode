
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0

        for house in houses:
            left = 0
            right = len(heaters) - 1

            while left <= right:
                mid = (left + right) // 2

                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1

            dist = float('inf')

            if left < len(heaters):
                dist = min(dist, heaters[left] - house)

            if right >= 0:
                dist = min(dist, house - heaters[right])

            ans = max(ans, dist)

        return ans
