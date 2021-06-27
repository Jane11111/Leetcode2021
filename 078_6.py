# -*- coding: utf-8 -*-
# @Time    : 2021-06-26 16:54
# @Author  : zxl
# @FileName: 078_6.py


class Solution:


    def subsets(self, nums ) :

        ans = [[]]
        for num in nums:
            l = len(ans)
            for i in range(l):
                tmp = [item for item in ans[i]]
                tmp.append(num)
                ans.append(tmp)
        return ans

obj = Solution()
nums = [1,2,3]
ans = obj.subsets(nums)
print(ans)