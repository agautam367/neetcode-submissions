class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]

        def dfs(opend,closed):
            #base case - open==close
            if opend==closed==n:
                res.append("".join(stack))
                return
            
            if opend<n:
                stack.append("(")
                dfs(opend+1,closed)
                stack.pop()
            if closed<opend:
                stack.append(")")
                dfs(opend,closed+1)
                stack.pop()
            
        dfs(0,0)
        return res

        