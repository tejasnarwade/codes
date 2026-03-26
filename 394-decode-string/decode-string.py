class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        num = 0

        for x in s:
            if x.isdigit():
                num = num * 10 + int(x)

            elif x == '[':
                stack.append((res, num))
                res = ""
                num = 0

            elif x == ']':
                prev_res, k = stack.pop()
                res = prev_res + k * res

            else:
                res += x

        return res