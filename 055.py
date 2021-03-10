# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 09:41
# @Author  : zxl
# @FileName: 055.py


"""
TODO 超时
"""

class Solution(object):


    def recursiveJump(self,nums,idx,dic):
        if idx >= len(nums):
            return False
        if idx == len(nums) - 1:
            return True
        if idx in dic:
            return dic[idx]
        val = nums[idx]
        for i in range(1,val+1):# 一直往下走
            if i+idx < len(nums):
                f = self.recursiveJump(nums,i+idx,dic)
                if f:
                    return f
                dic[i+idx]= False
            else:
                break
        return False


    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        f = False
        for i in range(len(nums)-1):
            if nums[i] == 0:
                f = True
                break
        if f: #包含0
            return self.recursiveJump(nums,0,{})
        return True


obj = Solution()
nums = [3,2,1,0,4]
f = obj.canJump(nums)
print(f)


