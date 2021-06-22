class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res=False
        used=[[0 for i in range(len(board[0]))] for j in range(len(board))]
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(cnt, x, y):
            ret=False
            if word[cnt]==board[x][y] and used[x][y]==0:
                if cnt==len(word)-1:
                    return True
                used[x][y]=1
                for i in range(4):
                    xn,yn=x+dir[i][0],y+dir[i][1]
                    if 0<=xn<len(board) and 0<=yn<len(board[0]):
                        ret=ret or dfs(cnt+1,xn,yn)
                used[x][y]=0
            return ret
        for i in range(len(board)):
            for j in range(len(board[0])):
                res=res or dfs(0,i,j)
        return res
            
