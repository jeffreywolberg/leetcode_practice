from collections import deque

class Solution:
    def dfs(self, grid, y, x):
        if x < 0 or x >= len(grid[0]):
            return
        elif y < 0 or y >= len(grid):
            return
        if grid[y][x] == "0":
            return
        
        grid[y][x] = "0"
        self.dfs(grid, y, x+1) # right
        self.dfs(grid, y-1, x) # up
        self.dfs(grid, y, x-1) # left
        self.dfs(grid, y+1, x) # up
    
    def bfs(self, grid, y, x):
        queue = deque([(y,x)])
        while queue:
            y, x = queue.popleft()
            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
                continue
            elif grid[y][x] == "1":
                grid[y][x] = "0"
                queue.append((y, x+1))
                queue.append((y-1, x))
                queue.append((y, x-1))
                queue.append((y+1, x))
        
            
        
    def numIslands(self, grid: List[List[str]]) -> int:
        # numIslands = 0
        # for y in range(len(grid)):
        #     for x in range(len(grid[0])):
        #         if grid[y][x] == "1":
        #             self.dfs(grid, y, x)
        #             numIslands += 1
        # return numIslands
    
        numIslands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    self.bfs(grid, y, x)
                    numIslands += 1
        return numIslands