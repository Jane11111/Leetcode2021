# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 11:35
# @Author  : zxl
# @FileName: Offer051_2.py



class Solution:


    def mergeSort(self,nums,i,j):

        if i==j:
            return 0
        if i>j:
            return 0
        m = (i+j)//2
        n1 = self.mergeSort(nums,i,m)
        n2 = self.mergeSort(nums,m+1,j)
        n3 = self.merge(nums,i,m,j)
        return n1+n2+n3


    def merge(self,nums,i,m,j):

        lst1 = nums[i:m+1]
        lst2 = nums[m+1:j+1]
        p = i
        s1 = 0
        s2 = 0
        cnt=0

        while p<=j:
            if s1 == len(lst1):
                while p<=j:
                    nums[p] = lst2[s2]
                    p+=1
                    s2+=1
            elif s2 == len(lst2):
                while p<=j:
                    nums[p] = lst1[s1]
                    p+=1
                    s1+=1
            else:
                if lst1[s1]<=lst2[s2]:
                    nums[p] = lst1[s1]
                    p+=1
                    s1+=1
                else:
                    nums[p] = lst2[s2]
                    s2+=1
                    p+=1
                    cnt+= len(lst1)-s1
        return cnt



    def reversePairs(self, nums ) -> int:


        ans = self.mergeSort(nums,0,len(nums)-1)
        return ans

