class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}
        for i in range(n):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
        return []

# optimal approach (Hashmmap or complement lookup)
'''
This works on the principle:

target = a + b

If we know a,
then b = target - a
We store numbers we have already seen in a dictionary

For each element:
1. Compute diff = target - current_number
2. If diff exists in the dictionary → pair found
3. Otherwise store current_number with its index
'''



# brute force using nested loops
'''
Check every pair in the array.

Fix one element (left) and check all elements after it (right).

nums[left] + nums[right] == target
'''

'''
for left in range(n):
    for right in range(left+1, n):
        if nums[left] + nums[right] == target:
            return [left, right]
return []
'''

