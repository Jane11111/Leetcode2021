# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 22:03
# @Author  : zxl
# @FileName: 078_4.py



class Solution:

    def recursiveFind(self,nums,idx):
        if idx == len(nums):
            return [[]]
        ans = []
        lst = self.recursiveFind(nums,idx+1)
        for sub_lst in lst:
            ans.append(sub_lst)
            tmp = sub_lst[:]
            tmp.insert(0,nums[idx])
            ans.append(tmp)
        return ans

    def subsets(self, nums ) :
        ans = self.recursiveFind(nums,0)
        return ans

obj = Solution()
nums = [1,2,3]
ans = obj.subsets(nums)
print(ans)
