class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if num[i] in "13579":  # odd digit check
                return num[:i+1]
        return ""