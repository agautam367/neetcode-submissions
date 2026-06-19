class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}

        for i,num in enumerate(nums):
            ans[num]=i
        
        for i,num in enumerate(nums):
            diff = target-num
            if diff in nums and ans[diff]!=i:
                return [i,ans[diff]]
        return []
