class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hts={}
        htt={}
        for x in s:
            hts[x]=hts.get(x,0)+1
        for x in t:
            htt[x]=htt.get(x,0)+1
        for c,cnt in hts.items():
            if htt.get(c,0)!=cnt:
                return False
        return True




        