# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# ==== Constraints ====

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        # use DFS or BFS to clear '1' once i, j visits a '1'
        num_islands = 0
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_islands += 1
                    q.append((i, j))
                    self.bfs(grid, q, m, n)

        return num_islands

    def bfs(self, grid, q, m, n):
        # use BFS to clear graph of '1'

        while q:  # while q != []
            k, l = q.pop(0)
            grid[k][l] = "0"
            # if there's adjacent node, add it to q
            if k + 1 < m and grid[k + 1][l] == "1":
                grid[k + 1][l] = "0"
                q.append((k + 1, l))
            if k - 1 >= 0 and grid[k - 1][l] == "1":
                grid[k - 1][l] = "0"
                q.append((k - 1, l))
            if l + 1 < n and grid[k][l + 1] == "1":
                grid[k][l + 1] = "0"
                q.append((k, l + 1))
            if l - 1 >= 0 and grid[k][l - 1] == "1":
                grid[k][l - 1] = "0"
                q.append((k, l - 1))


sol = Solution()

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(sol.numIslands(grid))

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(sol.numIslands(grid))

grid = [
    ["1", "1", "1", "1", "1", "1"],
    ["1", "0", "0", "0", "0", "1"],
    ["1", "0", "1", "1", "0", "1"],
    ["1", "0", "0", "0", "0", "1"],
    ["1", "1", "1", "1", "1", "1"],
]
print(sol.numIslands(grid))

grid = [
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "0",
        "1",
        "1",
    ],
    [
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
    ],
    [
        "1",
        "0",
        "1",
        "1",
        "1",
        "0",
        "0",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "0",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
    ],
    [
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "0",
        "0",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
]
print(sol.numIslands(grid))