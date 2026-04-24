class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            #Backtracking steps:
            #1. make a decision
            #2. recursion
            #3. it touches the base case
            #4. undo decision
            if i>=len(nums):
                #it touches the base case and we append it to the res
                res.append(subset.copy())
                return
            #we don't include a number
            dfs(i+1)

            # we include a number
            subset.append(nums[i])
            dfs(i+1)
            #we undo the decision
            subset.pop()
        dfs(0)
        return res