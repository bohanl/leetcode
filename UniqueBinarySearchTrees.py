class Solution:
    def count(self, n, T):
        if T[n] != -1:
            return T[n]

        T[n] = 0
        for i in xrange(1,n+1):
            T[n] += (self.count(i-1, T) * self.count(n-i,T))

        return T[n]

    # DP: top-down with memorization
    def num_trees_top_down(self, n):
        T = [-1] * (n+1)
        T[0], T[1] = 1, 1
        
        return self.count(n, T)

    # DP: bottom-up
    def num_trees_bottom_up(self, n):
        T = [0] * (n+1)
        T[0], T[1] = 1, 1

        for k in xrange(2, len(T)):
            for j in xrange(k/2):
                T[k] += 2*T[j]*T[k-1-j]
            if k % 2:
                T[k] += T[k/2]*T[k/2]

        return T[-1]

    # @return an integer
    def numTrees(self, n):
        return self.num_trees_top_down(n)