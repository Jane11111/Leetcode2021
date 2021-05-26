# -*- coding: utf-8 -*-
# @Time    : 2021-05-19 11:15
# @Author  : zxl
# @FileName: 179_2.py


class Solution:


    def quicksort(self,nums,i,j):
        if i>=j:
            return
        p = self.partition(nums,i,j)
        self.quicksort(nums,i,p-1)
        self.quicksort(nums,p+1,j)


    def partition(self,nums,m,n):

        x = nums[n]
        p = m-1
        for i in range(m,n):
            if nums[i]+x>x+nums[i]:
                p+=1
                nums[p],nums[i] = nums[i],nums[p]
        p+=1
        nums[p],nums[n] = nums[n],nums[p]
        return p

    def largestNumber(self, nums ) -> str:

        lst = [str(num) for num in nums]
        self.quicksort(lst,0,len(lst)-1)
        s = ''
        for num in lst:
            s+=num
        i = 0
        while i<len(s) and s[i] == '0':
            i+=1
        if i == len(s):
            s = '0'
        else:
            s = s[i:]
        return s

