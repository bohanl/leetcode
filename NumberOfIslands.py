class Solution:
    def get_neighbors(self, i, j, m, n):
        neighbors = []
        if i > 0: neighbors.append((i-1,j))
        if i < m-1: neighbors.append((i+1,j))
        if j > 0: neighbors.append((i,j-1))
        if j < n-1: neighbors.append((i,j+1))
        return neighbors

    def bfs(self, grid, visited, i, j, m, n):
        q = collections.deque([(i,j)])
        while q:
            ii, jj = q.popleft()
            for ni, nj in self.get_neighbors(ii, jj, m, n):
                if grid[ni][nj] == '1' and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
            visited[ii][jj] = 2

    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        count = 0
        if not grid:
            return count

        m, n = len(grid), len(grid[0])
        visited = [[0]*n for i in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    self.bfs(grid, visited, i, j, m, n)
                    count += 1

        return count
