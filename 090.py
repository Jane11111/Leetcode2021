# -*- coding: utf-8 -*-
# @Time    : 2021-03-25 20:04
# @Author  : zxl
# @FileName: 090.py

class Solution(object):

    def recursiveFind(self,nums):
        ans = []

        if len(nums) == 0:
            ans.append([])
            return ans

        if len(nums) == 1:
            ans.extend([[],[nums[0]]])
            return ans
        i = 1
        while i<len(nums) and nums[i] == nums[i-1]:
            i+=1

        left_comb = []
        for k in range(i+1):
            left_comb.append(nums[:k])

        sub_ans_lst = self.recursiveFind(nums[i:])
        for sub_ans in sub_ans_lst:
            for left_lst in left_comb:
                l1 = [item for item in left_lst]
                l1.extend(sub_ans)
                ans.append(l1)
        return ans



    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = self.recursiveFind(nums)
        return ans

obj = Solution()
nums = [1,2,2]
ans = obj.subsetsWithDup(nums)
print(ans)

