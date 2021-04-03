# -*- coding: utf-8 -*-
# @Time    : 2021-03-25 15:49
# @Author  : zxl
# @FileName: 047.py


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) == 1:
            return [nums]

        ans = []
        i = 0
        while i < len(nums):
            num = nums[i]
            tmp = nums[:i] + nums[i+1:]
            sub_ans = self.permuteUnique(tmp)
            for lst in sub_ans:
                a = [num]
                a.extend(lst)
                ans.append(a)
            i+=1
            while i<len(nums) and nums[i] == nums[i-1]:
                i+=1
        return ans

obj = Solution()
nums = [1,2,3]
ans = obj.permuteUnique(nums)
print(ans)