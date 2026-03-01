class Solution:
    def secondHighest(self, s: str) -> int:
        dict1={}
        for x in s:

            if x.isnumeric():
                dict1[int(x)] = dict1.get(int(x),0)+1
        sd = sorted(dict1.items())
        if len(sd)>=2:
            return sd[-2][0]
        else:
            return -1

