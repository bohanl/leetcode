class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        # assuming matrix is a square matrix
        n = len(matrix)

        for layer in xrange(n/2):
            last = n-layer-1
            for i in xrange(layer,last):
                # save top
                top = matrix[layer][i]
                # left -> top
                matrix[layer][i] = matrix[n-1-i][layer]
                # bottom -> left
                matrix[n-1-i][layer] = matrix[last][n-1-i]
                # right -> bottom
                matrix[last][n-1-i] = matrix[i][last]
                # top -> right
                matrix[i][last] = top

        return matrix
