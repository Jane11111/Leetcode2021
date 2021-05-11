# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 20:10
# @Author  : zxl
# @FileName: 377.py

class Solution:

    def recursiveFind(self,nums,target,dic):
        if target in dic:
            return dic[target]
        if target == 0:
            return 1
        if target <0:
            return 0
        ans = 0
        for num in nums:
            ans += self.recursiveFind(nums,target-num,dic)
        dic[target] = ans
        return ans


    def combinationSum4(self, nums, target):

        ans = self.recursiveFind(nums,target,{})
        return ans






obj = Solution()

nums = [4,2,3]
target = 32
ans = obj.combinationSum4(nums,target)
print(ans)




