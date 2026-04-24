class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        #leave the first number and continue the loop by doing this for all the nums
        perms=self.permute(nums[1:])
        res=[]
        for p in perms:
            for i in range(len(p)+1):
                p_copy=p.copy()
                #insert nums[0] at various indexes
                p_copy.insert(i,nums[0])
                res.append(p_copy)
        return res

        