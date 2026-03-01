class Solution:
    def selection_sort(self,nums):
        n=len(nums)
        for i in range(n-1):
            minx = i
            for j in range(i+1,n):
                if nums[j]<nums[minx]:
                    minx = j
            nums[i],nums[minx]=nums[minx],nums[i]
        return nums
    def check(self, nums: List[int]) -> bool:
        ognums=nums.copy()
        non_dec_order = self.selection_sort(nums)   #here non dec order means incresaing order array
        rotated = False
        for i in range(len(non_dec_order)):
            if non_dec_order==ognums or non_dec_order[i:]+non_dec_order[:i] == ognums:
                return True
        return False

        