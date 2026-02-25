class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxnum : int = len(nums)
        idealsum =0
        for i in range(0,maxnum+1):
            idealsum+=i

        rlsum = sum(nums)
        return idealsum - rlsum
        