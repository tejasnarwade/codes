class Solution:
    #author=tejasnarwade
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x = abs(x)
        ld : int=0
        rev:int = 0
        while x!=0:
            ld = x%10
            rev = (rev*10)+ld
            x=x//10
        rev = rev*sign
        if not (-2**31 <= rev <= 2**31-1):
            return 0
        return rev
