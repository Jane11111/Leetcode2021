# -*- coding: utf-8 -*-
# @Time    : 2021-06-27 10:15
# @Author  : zxl
# @FileName: 087_2.py




class Solution:



    def isScramble(self, s1: str, s2: str) -> bool:



        n = len(s1)
        dp = []
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append([True for k in range(n+1)])
            dp.append(tmp)
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]


        for l in range(2,n+1):
            for i in range(n):
                for j in range(n):
                    e1 = i+l-1
                    e2 = j+l-1
                    if e1>=n or e2>=n:
                        break
                    f = False
                    for k in range(i+1,e1+1):
                        f1 = dp[i][j][k-i]
                        f2 = dp[k][j+(k-i)][l-(k-i)]

                        f3 = dp[i][e2-(k-i)+1][k-i]
                        f4 = dp[k][j][l-(k-i)]

                        if (f1 and f2) or(f3 and f4):
                            f = True
                            break
                    dp[i][j][l] = f
        return dp[0][0][n]


obj = Solution()
s1 = "abcdbdacbdac"
s2 = "bdacabcdbdac"

ans = obj.isScramble(s1,s2)
print(ans)






