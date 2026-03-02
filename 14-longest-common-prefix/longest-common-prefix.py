class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        newstrs = sorted(strs)
        first = newstrs[0]
        last= newstrs[-1]
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return lcp
            lcp+=first[i]
        return lcp