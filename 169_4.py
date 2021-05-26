# -*- coding: utf-8 -*-
# @Time    : 2021-05-18 16:30
# @Author  : zxl
# @FileName: 169_4.py



class Solution:

    def divide(self,nums,i,j):
        if i == j:
            return nums[i]
        m = (i+j)//2
        num1 = self.divide(nums,i,m)
        num2 = self.divide(nums,m+1,j)

        num = self.judge(nums,i,j,num1,num2)
        return num

    def judge(self,nums,i,j,num1,num2):
        n1 = 0
        n2 = 0
        for k in range(i,j+1):
            if nums[k] == num1:
                n1+=1
            if nums[k] == num2:
                n2+=1
        if n1>n2:
            return num1
        else:
            return num2

    def majorityElement(self, nums ) -> int:

        ans = self.divide(nums,0,len(nums)-1)
        return ans


