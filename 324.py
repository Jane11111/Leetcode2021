# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 17:21
# @Author  : zxl
# @FileName: 324.py


class Solution(object):

    # def quick_sort(self,nums,p,r):
    #     if p>=r:
    #         return
    #     q = self.partition(nums,p,r)
    #     self.quick_sort(nums,p,q-1)
    #     self.quick_sort(nums,q+1,r)
    #
    # def partition(self,nums,p,r):
    #
    #
    #     x = nums[r]
    #     i = p-1
    #     for j in range(p,r):
    #         if nums[j]<x:
    #             nums[i+1],nums[j] = nums[j],nums[i+1]
    #             i+=1
    #     nums[i+1],nums[r] = nums[r],nums[i+1]
    #     return i+1


    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # self.quick_sort(nums,0,len(nums)-1)
        # i = 1
        # j = (len(nums)+1)//2
        # while j<=len(nums)-1:
        #     v = nums.pop(j)
        #     nums.insert(i,v)
        #     i+=2
        #     j+=1
        nums.sort(reverse=True)
        nums[::2],nums[1::2] = nums[len(nums)//2:],nums[:len(nums)//2]



nums = [1,5,1,1,6,4]
obj =Solution()
obj.wiggleSort(nums)
print(nums)