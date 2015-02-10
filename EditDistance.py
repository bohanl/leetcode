class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        
        T = [[0]*(n+1) for i in xrange(m+1)]
        
        for j in xrange(1, n+1):
            T[0][j] = j
        
        for i in xrange(1, m+1):
            T[i][0] = i
        
        for i in xrange(1,m+1):
            for j in xrange(1,n+1):
                if word1[i-1] == word2[j-1]:
                    T[i][j] = T[i-1][j-1]
                else:
                    T[i][j] = min(T[i-1][j], T[i-1][j-1], T[i][j-1])+1
        
        return T[-1][-1]