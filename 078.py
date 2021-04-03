# -*- coding: utf-8 -*-
# @Time    : 2021-03-25 19:59
# @Author  : zxl
# @FileName: 078.py


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if len(nums) == 1:
            ans.extend([[],[nums[0]]])
        else:
            sub_ans_lst = self.subsets(nums[1:])
            for sub_ans in sub_ans_lst:
                lst1 = [item for item in sub_ans]
                lst1.append(nums[0])
                ans.append(sub_ans)
                ans.append(lst1)
        return ans

obj = Solution()
nums = [0]
ans = obj.subsets(nums)
print(ans)

