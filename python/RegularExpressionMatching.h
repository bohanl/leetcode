class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        if (*p == '\0') {
            return *s == '\0';
        }

        if (*(p+1) == '*') {
            while (*s != '\0' && (*s == *p || *p == '.')) {
                if (isMatch(s, p+2)) {
                    return true;
                }
                s = s+1;
            }
            return isMatch(s,p+2);
        }

        return (*s != '\0' && (*s == *p || *p == '.')) &&
            isMatch(s+1,p+1);
    }
};
