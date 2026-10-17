class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            dq = deque([(r, c)])

            while dq: 
                row, col = dq.popleft()
                #check neighbouring cells
                for dir_r, dir_c in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    new_r, new_c = dir_r+row, dir_c+col

                    if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols or grid[new_r][new_c] == "0":
                        continue
                    grid[new_r][new_c] = "0"
                    #push only valid cells
                    dq.append((new_r, new_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)

        return islands




