class Solution:
    def combinationSum(self, candidates, target):
        
        answer = []

        def find_combinations(start, current, total):
            
            if total == target:
                answer.append(current.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                
                number = candidates[i]
                
                current.append(number)

                # i is passed again because we can reuse the same number
                find_combinations(i, current, total + number)

                current.pop()

        find_combinations(0, [], 0)

        return answer