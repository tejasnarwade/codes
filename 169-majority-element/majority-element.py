class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n= len(nums)
        maj_ele=[0,0]
        avgplus = n/2
        mydict : dict[int,int]={}
        for x in nums:
            mydict[x] = mydict.get(x,0)+1
        
        for k,v in mydict.items():
            if v>maj_ele[1]:
                maj_ele[0]=k
                maj_ele[1]=v
        return int(maj_ele[0])

        