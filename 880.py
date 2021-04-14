# -*- coding: utf-8 -*-
# @Time    : 2021-04-06 21:18
# @Author  : zxl
# @FileName: 880.py


class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:

        s = ''
        for i in range(len(S)):
            if S[i] >= '0' and S[i] <= '9':
                n = int(S[i])
                s = s*n
                # for k in range(n-1):
                #     s+=s
            else:
                s+=S[i]
            if len(s)>=K:
                return s[K-1]

obj = Solution()
S="a2b3c4d5e6f7g8h9"
K=10
ans = obj.decodeAtIndex(S,K)
print(ans)


