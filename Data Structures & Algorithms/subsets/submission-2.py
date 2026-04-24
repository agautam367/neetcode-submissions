class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        #Backtracking- define a base case
        #make a decision
        #recursion
        #undo decision
        #recursion

        def dfs(i):
            if i>=len(nums):
                
                res.append(subset.copy())
                return
            #made a decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            #undo the decision to include nums[i]
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res
        