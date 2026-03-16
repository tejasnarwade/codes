class Solution:
    def countCommas(self, n: int) -> int:
        cnt = 0      # ithe total comma count initialize kela
        p = 1000     # ithe pahila comma 1000 pasun suru hoto

        while p <= n:   # jo paryant p n peksha motha nahi to paryant loop chalel
            
            # p pasun n paryant je numbers aahet tyat ek comma contribute hoil
            cnt += n - p + 1
            
            # pudhcha comma level (1000 -> 1000000 -> 1000000000 ...)
            p *= 1000

        return cnt   # final comma count return karto