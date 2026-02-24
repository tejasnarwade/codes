class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        ld : int=0
        rev : int =0
        og_x = x
        while(x!=0):
            ld = x%10
            rev = (rev*10)+ld
            x = x//10
        if -2**31 >= rev >= 2**31-1:
            return False
        return True if og_x==rev else False        