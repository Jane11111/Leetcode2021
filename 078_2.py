# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 21:52
# @Author  : zxl
# @FileName: 078_2.py


class Solution:

    def recursiveFind(self,nums,idx,lst):

        if idx == len(nums):
            return [lst]
        ans = []
        # for i in range(idx,len(nums)):
        tmp1 = lst[:]
        tmp2 = lst[:]
        ans1 = self.recursiveFind(nums,idx+1,tmp1)
        tmp2.append(nums[idx])
        ans2 = self.recursiveFind(nums,idx+1,tmp2)
        ans.extend(ans1)
        ans.extend(ans2)
        return ans


    def subsets(self, nums ) :

        ans = self.recursiveFind(nums,0,[])
        return ans

obj = Solution()
nums = [0]
ans = obj.subsets(nums)
print(ans)

