# -*- coding: utf-8 -*-
# @Time    : 2021-04-06 22:44
# @Author  : zxl
# @FileName: 880_2.py


class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:

        N = 0
        for i in range(len(S)):
            if S[i]>='0' and S[i]<='9':
                N = N*(int(S[i]))
            else:
                N+=1

        for i in range(len(S)-1,-1,-1):
            if S[i] >= '0' and S[i]<='9':
                N /= int(S[i])
                if K>N:
                    K = K%N
            else:
                if K%N == 0 :
                    return S[i]
                N-=1

obj = Solution()
S = "leet2code3"
K = 10
ans = obj.decodeAtIndex(S,K)
print(ans)