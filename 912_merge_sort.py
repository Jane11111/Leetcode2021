# -*- coding: utf-8 -*-
# @Time    : 2021-05-15 10:47
# @Author  : zxl
# @FileName: 912_merge_sort.py



# 时间复杂度 O(nlogn)
# 空间复杂度 O(n) tmp数组可以通用

class Solution:

    def mergeSort(self,nums,i,j):
        if i>=j:
            return
        m = (i+j)//2
        self.mergeSort(nums,i,m)
        self.mergeSort(nums,m+1,j)
        self.merge(nums,i,m,j)

    def merge(self,nums,l,m,r):

        lst1 = nums[l:m+1]
        lst2 = nums[m+1:r+1]

        p = l
        i = 0
        j = 0
        while p<=r:
            if i == len(lst1):
                while p<=r:
                    nums[p] = lst2[j]
                    p+=1
                    j+=1
            elif j== len(lst2):
                while p<=r:
                    nums[p] = lst1[i]
                    p+=1
                    i+=1
            else:
                if lst1[i]<lst2[j]:
                    nums[p] = lst1[i]
                    p+=1
                    i+=1
                else:
                    nums[p] = lst2[j]
                    p+=1
                    j+=1




    def sortArray(self, nums ) :

         self.mergeSort(nums,0,len(nums)-1)
         return nums