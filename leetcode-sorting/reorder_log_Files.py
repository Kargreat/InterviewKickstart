import string
from typing import List

ip_ = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
ip_ = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        numeric=[]
        alpha = []
        for log in logs:
            if str(log).split(" ")[1].isnumeric():
                numeric.append(log)
            else:
                alpha.append(log)
        return sorted(alpha, key=lambda ini_string: ''.join([i for i in ini_string if not i.isdigit()]) ) + numeric


if __name__ == '__main__':
    sol = Solution()
    print(sol.reorderLogFiles(ip_))