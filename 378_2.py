# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 17:20
# @Author  : zxl
# @FileName: 378_2.py





class Solution:

    def countNum(self,matrix,mid,k):

        i = len(matrix)-1
        j = 0
        count=0
        while i>=0 and j<len(matrix):

            if matrix[i][j]<=mid:
                count+=(i+1)
                j+=1
            else:
                i-=1
        return count>=k


    def kthSmallest(self, matrix , k: int) -> int:


        l = matrix[0][0]
        r = matrix[-1][-1]

        while l<r:
            mid = (l+r)//2
            if self.countNum(matrix,mid,k):
                r = mid
            else:
                l = mid+1
        return l



