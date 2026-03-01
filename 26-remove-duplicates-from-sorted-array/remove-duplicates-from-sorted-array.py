class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        i=0
        seen =[]
        for num in nums:
            if num not in seen:
                seen.append(num)
        for i in range(len(seen)):
            nums[i]=seen[i]        
            
        k = len(seen)      
        return k