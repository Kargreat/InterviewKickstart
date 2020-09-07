ip_ = str("40")


class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0' or s.__contains__('00'):
            return 0

        decodings = dict()
        decodings[0] = 1
        if len(s) > 1:
            if int(s[0]+s[1]) <= 26:
                if s[1] == '0':
                    decodings[1] = decodings[0]
                else:
                    decodings[1] = decodings[0] + 1
            else:
                if s[1] == '0':
                    return 0
                else:
                    decodings[1] = decodings[0]
        else:
            decodings[1] = decodings[0]

        if len(s) > 2:
            for i in range(2, len(s)):
                if s[i] == '0':
                    if int(s[i-1] + s[i]) <= 26:
                        decodings[i] = decodings[i-1] = decodings[i-2]
                    else:
                        return 0
                else:
                    decodings[i] = decodings[i - 1]
                    if s[i-1] != '0' and int(s[i-1] + s[i]) <= 26:
                        decodings[i] += decodings[i-2]


        return list(decodings.values())[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numDecodings(ip_))
