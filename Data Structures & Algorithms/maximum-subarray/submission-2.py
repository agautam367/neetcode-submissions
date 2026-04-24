class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #use kadane's algo for this
        # start at first element
        #if the sum at the prev element is negative then start new array
        #else if the sum at prev element is positive then continue the array

        res=nums[0]
        maxEnding= nums[0]
        for i in range(1,len(nums)):
            maxEnding=max(maxEnding + nums[i],nums[i])
            res=max(res,maxEnding) 
        return res       