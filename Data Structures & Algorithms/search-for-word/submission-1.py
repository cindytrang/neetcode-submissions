class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(board)
        cols = len(board[0])

        visited = set()
        def dfs(row, col, word): 
            if not word:
                return True
            if (row, col) in visited:  # ← Already visited in this path
                return False
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != word[0]:
                return False 
            visited.add((row, col))
            for r_dir, c_dir in directions:
               if dfs(row+r_dir, c_dir+col, word[1:]):
                    return True #  False ## FORGOT ABPUT THIs return
            visited.remove((row, col))
            return False ## FORGOT ABPUT THIs return


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, word):  ## FORGOT ABPUT THIs return
                        return True
                        ## FORGOT ABPUT THIs return
        # end of loop the word was not found
        return False