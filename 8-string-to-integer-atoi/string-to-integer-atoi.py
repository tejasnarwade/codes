class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        isneg = 0

        s = s.lstrip()

        if not s:
            return 0

        if s[0] == '-':
            isneg = 1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        for x in s:
            if not x.isnumeric():
                break
            result = result * 10 + int(x)

        if isneg:
            result = -result

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result