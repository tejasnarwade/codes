class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hm = {}
        for x in nums:
            hm[x]=hm.get(x,0)+1
        return int(''.join([str(x) for x,y in hm.items() if y!=2 ]))