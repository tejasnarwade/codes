class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
        s = ''.join([c for c in s if c.isalnum()]).strip().lower().replace(" ","")
        return True if s[::-1]==s else False
        