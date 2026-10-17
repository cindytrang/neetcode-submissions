class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if r < 0 or c < 0 or c >= cols or r >= rows:
                return
            if grid[r][c] == "0":
                return
            #explore directions
            grid[r][c] = "0"
            for dir_r, dir_c in [[0,1], [0, -1], [1, 0], [-1, 0]]:
                dfs(r+dir_r, c+dir_c)

            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands



