class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        n = len(ratings)

        candies = [1]*n

        for i in xrange(1,n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1

        for i in xrange(n-1,0,-1):
            if ratings[i] < ratings[i-1] and candies[i] >= candies[i-1]:
                candies[i-1] = candies[i]+1

        return sum(candies)