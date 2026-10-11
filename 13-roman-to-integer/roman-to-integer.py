
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            current = values[s[i]]

            if i < len(s) - 1:
                next_value = values[s[i + 1]]

                if current < next_value:
                    total -= current
                else:
                    total += current
            else:
                total += current

        return total
