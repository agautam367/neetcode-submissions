class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=set()
        sol=[]
        def dfs(i):
            if i>=len(nums):
                res.add(tuple(sol.copy()))
                return
            #don't include and perform dfs
            dfs(i+1)
            #include and perform dfs
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()
        nums.sort()
        dfs(0)
        return [list(i) for i in res]
        