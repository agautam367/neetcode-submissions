from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq=Counter(nums)
        return any(val>1 for key,val in freq.items())

        