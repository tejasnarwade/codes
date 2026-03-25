class Solution:

    #we will be using two pointer pattern as we need to find pairs with maximum sum where left one being greater
    def maxArea(self, height: List[int]) -> int:
        l=0   # we will start at 0 the left pointer
        r=len(height)-1      #right ponter will start from end index
        max_water=0
        while l<r:  
            # until right index not equal to left index
            h = min(height[l],height[r]) #height will be minimum one between height[l] and height[r]
            w = r - l     #width is distance between 2 pointers
            max_water = max(max_water,h*w)
            # jr left value lesser ahe tr left as comapred to right such that we have to acccumulate maximum amount of water so need maximum height[left]
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return max_water
        


        #author:tejasnarwade
        '''
for my reference here is the template for array two pointer:

    def two_pointer(arr):
    l=0 
    r = len(arr) - 1
    ans = 0   # or inf / [] depending on problem
    
    while l < r:
        # 1. compute result
        val = min(arr[l], arr[r]) * (r - l)   # change logic per problem
        ans = max(ans, val)
        
        # 2. move pointer (KEY PART)
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    
    return ans



        '''

