# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 16:28
# @Author  : zxl
# @FileName: 152.py

# 超时

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        m = len(nums)
        arr = []
        ans = float('-inf')
        for i in range(m):
            arr.append([0 for j in range(m)])
            arr[i][i] = nums[i]
            ans = max(ans,arr[i][i])

        for l in range(2,m+1):
            for i in range(m):
                j = i+l-1
                if j>= m:
                    continue
                arr[i][j] = arr[i][j-1]*nums[j]
                ans = max(ans,arr[i][j])
        return ans



obj = Solution()
nums = [2,3,-2,4]
ans = obj.maxProduct(nums)
print(ans)




