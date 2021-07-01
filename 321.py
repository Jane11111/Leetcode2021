# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 20:58
# @Author  : zxl
# @FileName: 321.py

# O(M*N*K)
# TODO 超时

class Solution:
    def maxNumber(self, nums1 , nums2 , k: int) :

        n1 = len(nums1)
        n2 = len(nums2)

        dp = []
        for i in range(n1+1):
            mat = []
            for j in range(n2+1):
                mat.append([' '*p for p in range(k+1)])
            dp.append(mat)

        for i in range(n1-1,-1,-1):
            l = n1-i
            for p in range(1,min(l,k)+1):
                if l == 1:
                    dp[i][n2][p] = str(nums1[i])
                else:
                    dp[i][n2][p] = max(dp[i+1][n2][p],str(nums1[i])+dp[i+1][n2][p-1])
        for j in range(n2-1,-1,-1):
            l = n2-j
            for p in range(1,min(l,k)+1):
                if l == 1:
                    dp[n1][j][p] = str(nums2[j])
                else:
                    dp[n1][j][p] = max(dp[n1][j+1][p],str(nums2[j])+dp[n1][j+1][p-1])

        for i in range(n1-1,-1,-1):
            l1 = n1-i
            for j in range(n2-1,-1,-1):
                l2 = n2-j

                for p in range(1,min(l1+l2,k)+1):

                    s = max(dp[i][j+1][p],dp[i+1][j][p],
                            str(nums2[j])+dp[i][j+1][p-1],
                            str(nums1[i])+dp[i+1][j][p-1])
                    if p>=2:
                        s = max(s,str(nums1[i])+str(nums2[j])+dp[i+1][j+1][p-2],
                                str(nums2[j])+str(nums1[i])+dp[i+1][j+1][p-2])
                    dp[i][j][p] = s
        ans = [int(c) for c in dp[0][0][k]]
        return ans

obj = Solution()
nums1 = [3,9]
nums2 = [8,9]
k = 3
ans = obj.maxNumber(nums1,nums2,k)
print(ans)