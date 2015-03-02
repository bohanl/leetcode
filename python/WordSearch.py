class Solution:

    def backtrack(self, board, m, n, word, i, j, visited):
        if not word:
            return True

        if i<0 or i>=m or j<0 or j>=n:
            return False

        if visited[i][j] or board[i][j] != word[0]:
            return False

        visited[i][j] = True

        found = self.backtrack(board, m, n, word[1:], i+1, j, visited)
        if not found:
            found = self.backtrack(board, m, n, word[1:], i-1, j, visited)
        if not found:
            found = self.backtrack(board, m, n, word[1:], i, j+1, visited)
        if not found:
            found = self.backtrack(board, m, n, word[1:], i, j-1, visited)

        visited[i][j] = False

        return found

    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        m, n = len(board), len(board[0])

        visited = [[False]*n for i in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                if self.backtrack(board,m,n,word,i,j,visited):
                    return True

        return False