class Solution:
    def _is_valid_pair(self, c1, c2):
        return (c1 == '(' and c2 == ')') or \
               (c1 == '{' and c2 == '}') or \
               (c1 == '[' and c2 == ']')

    # @return a boolean
    def isValid(self, s):
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack or not self._is_valid_pair(stack.pop(), c):
                    return False

        return not stack