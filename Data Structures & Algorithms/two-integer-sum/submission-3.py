class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output={}
        
        for i,num in enumerate(nums):
            output[num]=i
        
        for i,num in enumerate(nums):
            diff = target-num
            if diff in output and output[diff]!=i:
                return [i,output[diff]]
        return []
