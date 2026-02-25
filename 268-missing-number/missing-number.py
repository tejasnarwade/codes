class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n : int = len(nums)
        idealsum = n*(n+1)//2
        #for i in range(0,maxnum+1):
            #idealsum+=i

        rlsum = sum(nums)
        return idealsum - rlsum
        