KEYPAD = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
}


class Solution:

    def backtrack(self, a, digits, n, k, res):
        if k == n:
            res.append(''.join(a))
            return

        candidates = KEYPAD[int(digits[k])]
        for c in candidates:
            a.append(c)
            self.backtrack(a, digits, n, k+1, res)
            a.pop()

    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        a, res = [], []
        n, k = len(digits), 0

        self.backtrack(a, digits, n, k, res)

        return res