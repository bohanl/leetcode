ass Solution:
    def get_neighbors(self, i, j, m, n):
        neighbors = []

        if i > 0: neighbors.append((i-1,j))
        if i < m-1: neighbors.append((i+1,j))
        if j > 0: neighbors.append((i,j-1))
        if j < n-1: neighbors.append((i,j+1))

        return neighbors

    def bfs(self, board, visited, i, j, m, n):
        q = collections.deque([(i,j)])
        flip_q, flip = collections.deque([]), True
        while q:
            ii, jj = q.popleft()
            flip_q.append((ii, jj))
            if ii == 0 or ii == m-1 or jj == 0 or jj == n-1:
                flip = False
            for ni, nj in self.get_neighbors(ii, jj, m, n):
                if board[ni][nj] == 'O' and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
            visited[ii][jj] = 2

        if flip:
            while flip_q:
                ii, jj = flip_q.popleft()
                board[ii][jj] = 'X'

    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return

        m, n = len(board), len(board[0])
        visited = [[0]*n for i in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'O' and visited[i][j] == 0:
                    self.bfs(board, visited, i, j, m, n)
