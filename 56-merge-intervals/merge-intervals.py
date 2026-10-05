class Solution:
    def merge(self, intervals):
        intervals.sort()

        answer = []

        for interval in intervals:
            if not answer or answer[-1][1] < interval[0]:
                answer.append(interval)
            else:
                answer[-1][1] = max(answer[-1][1], interval[1])

        return answer