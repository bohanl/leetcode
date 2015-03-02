class Solution:
    def _backtrack(self, candidates, target, res, a):
        if target == 0:
            res.append(a[:])
            return

        if target < 0 or not candidates:
            return

        c = candidates[0]
        if target < c:
            return

        a.append(c)
        self._backtrack(candidates[1:], target-c, res, a)
        a.pop()

        i = 1
        while i < len(candidates) and candidates[i] == c: i += 1
        self._backtrack(candidates[i:], target, res, a)

    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()

        res, a = [], []
        self._backtrack(candidates, target, res, a)

        return res
