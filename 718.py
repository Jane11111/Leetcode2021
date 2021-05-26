# -*- coding: utf-8 -*-
# @Time    : 2021-05-24 15:43
# @Author  : zxl
# @FileName: 718.py



class Solution:
    def findLength(self, nums1 , nums2 ) -> int:

        m = len(nums1)
        n = len(nums2)
        dp = []
        for i in range(m+1):
            dp.append([0 for j in range(n+1)])

        ans = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = 0
                ans = max(ans,dp[i][j])
        return ans

obj = Solution()
nums1 = [0,1,1,1,1]
nums2 = [1,0,1,0,1]
ans = obj.findLength(nums1,nums2)
print(ans)



