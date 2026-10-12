
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1

        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        num = 0

        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            i += 1

        num *= sign

        low = -(2 ** 31)
        high = (2 ** 31) - 1

        if num < low:
            return low
        if num > high:
            return high

        return num
