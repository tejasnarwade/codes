class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp =list() 
        for x in nums:
            if x!=val:
                temp.append(x)
        nums.clear()
        for x in temp:
            nums.append(x)
        return len(nums)