class Solution:
    def isPalindrome(self, s: str) -> bool:
        ogs=s
        s = s.replace(" ", "").lower()
        s = ''.join([char for char in s if char.isalnum()])
        if s[::-1]==s:
            return True
        else: return False
        