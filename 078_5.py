# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 22:07
# @Author  : zxl
# @FileName: 078_5.py




class Solution:

    def subsets(self, nums):

        ans = [[]]
        for num in nums:
            l = len(ans)
            for i in range(l):
                tmp = ans[i][:]
                tmp.append(num)
                ans.append(tmp)
        return ans

obj = Solution()
nums = [1,2,3]
ans = obj.subsets(nums)
print(ans)