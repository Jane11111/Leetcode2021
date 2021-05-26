# -*- coding: utf-8 -*-
# @Time    : 2021-05-19 14:39
# @Author  : zxl
# @FileName: 315.py


class Solution:

    def mergeSort(self,nums,indices,i,j,lst):

        if i>=j:
            return
        m = (i+j)//2
        self.mergeSort(nums,indices,i,m,lst)
        self.mergeSort(nums,indices,m+1,j,lst)
        self.merge(nums,indices,i,m,j,lst)



    def merge(self,nums,indices,i,m,j,counts):

        lst1 = indices[i:m+1]
        lst2 = indices[m+1:j+1]
        p = i
        x = 0
        y = 0
        while p<= j:
            if x == len(lst1):
                while p<=j:
                    indices[p] = lst2[y]
                    p+=1
                    y+=1
            elif y == len(lst2):
                while p<=j:
                    indices[p] = lst1[x]
                    p+=1
                    x+=1
            else:
                if nums[lst1[x]]>nums[lst2[y]]:
                    counts[lst1[x]] += (len(lst2)-y)
                    indices[p] = lst1[x]
                    x+=1
                    p+=1
                else:
                    indices[p] = lst2[y]
                    y+=1
                    p+=1

    def countSmaller(self, nums ) :


        indices = [i for i in range(len(nums))]
        counts = [0 for i in range(len(nums))]
        self.mergeSort(nums,indices,0,len(nums)-1,counts)
        return counts

obj = Solution()
nums = [0,2,1]
ans = obj.countSmaller(nums)
print(ans)