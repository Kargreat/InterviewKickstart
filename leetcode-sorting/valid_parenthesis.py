ip_ = "([)]"

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        a = []
        for i in range(0, len(s)):
            if s[i] in ['{', '(', '[']:
                a.append(s[i])
            if s[i] in ['}', ')', ']']:
                if s[i] == '}':
                    if '{' in a:
                        a.remove('{')
                    else:
                        return False
                elif s[i] == ']':
                    if '[' in a:
                        a.remove('[')
                    else:
                        return False
                else:
                    if '(' in a:
                        a.remove('(')
                    else:
                        return False
        return True


if __name__ == '__main__':
    sol = Solution()

    print(sol.isValid(ip_))