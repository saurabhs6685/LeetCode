class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []

        def backtrack(start, target, path):
            if target == 0:
                ans.append(path.copy())
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):

                # same level par duplicate number skip
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # sorted hai, isliye aage ke numbers bhi bade honge
                if candidates[i] > target:
                    break

                path.append(candidates[i])

                # next index se start, same element dobara nahi
                backtrack(i + 1, target - candidates[i], path)

                path.pop()

        backtrack(0, target, [])
        return ans