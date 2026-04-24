class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return
            if i>=len(nums) or total>target:
                return
            #make a decision to include the number
            cur.append(nums[i])
            dfs(i,cur,total+nums[i])
            #undo the decision, don't include the number and perform dfs
            cur.pop()
            #it proceeds to the next number and doesn't include more entries of the same number
            dfs(i+1,cur,total)
        dfs(0,[],0)
        return res
        