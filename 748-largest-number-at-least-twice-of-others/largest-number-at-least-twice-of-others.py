class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)
        larEle = max(nums)
        notlar = False
        i=0
        while i<n:

            if nums[i]!=larEle:
                if not (larEle>=(nums[i])+nums[i]):
                    notlar = True
            i+=1
        if notlar:
            return -1
        else:
            return nums.index(larEle)

        