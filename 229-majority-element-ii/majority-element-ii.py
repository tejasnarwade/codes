class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #bruteforce
        #n = len(nums)
        #target = n/3
        #result=[]
        '''     brute force where i check frequency of each via nums.count(element)>target
        for x in nums:
            if nums.count(x)>target and x not in result:
                result.append(x)
        return result
        '''

        #optimal approach
        freqdict = {}
        for x in nums:
            freqdict[x]=freqdict.get(x,0)+1
        return [x for x,y in freqdict.items() if y>len(nums)//3]