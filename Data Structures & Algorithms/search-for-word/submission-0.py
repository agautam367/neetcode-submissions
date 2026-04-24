class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        visited = [[False for j in range(n)] for i in range(m)]
        def dfs(r,c,i):
            if i==len(word):
                return True
            if (r<0 or c<0 or r>=m or c>=n or visited[r][c] or board[r][c]!=word[i]):
                return False
            visited[r][c]=True
            res=(dfs(r+1,c,i+1) or 
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1))
            visited[r][c]=False
            return res

        for i in range(0,m):
            for j in range(0,n):
                if dfs(i,j,0):
                    return True
        return False