class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       return (len(nums)*(len(nums)+1)//2)-sum(nums)
        
        #formula: n*(n+1)/2---> gives us total sum of arrray of the number wasnt missing , so we will do idealsum-actual sum = missingnumber