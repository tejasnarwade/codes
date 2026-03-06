class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        triplets=[]
        nums.sort()

        for curr in range(n):
            if nums[curr]>0:
                pass #karan jar current > 0 mang tr sum 0 yenarch nay
            if curr>0 and nums[curr]==nums[curr-1]:
                continue

            left=curr+1
            right=n-1

            while left<right:

                sumres=nums[curr]+nums[left]+nums[right]

                if sumres>0:
                    right-=1

                elif sumres<0:
                    left+=1

                else:
                    triplets.append([nums[curr],nums[left],nums[right]])

                    left+=1
                    right-=1

                    while left<right and nums[left]==nums[left-1]:
                        left+=1

                    while left<right and nums[right]==nums[right+1]:
                        right-=1

        return triplets