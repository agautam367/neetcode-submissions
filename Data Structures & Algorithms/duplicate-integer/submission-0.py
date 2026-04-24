class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter=[]
        for i in nums:
            if i not in counter:
                counter.append(i)
        if len(counter)==len(nums):
            return False
        else:
            return True

         