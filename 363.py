# -*- coding: utf-8 -*-
# @Time    : 2021-06-21 14:59
# @Author  : zxl
# @FileName: 363.py



class Solution:

    #
    def biSearch(self,sorted_arr,r_val,k):


        l = 0
        r = len(sorted_arr)-1

        while l<r:
            m = (l+r)//2
            if r_val - sorted_arr[m]>k:
                l = m+1
            else:
                r = m
        v = r_val - sorted_arr[l]

        if v<=k:
            return v

        return float('-inf')



    def biInsert(self,sorted_arr,v):

        if v>=sorted_arr[-1]:
            sorted_arr.append(v)
            return

        l = 0
        r = len(sorted_arr)-1
        while l<r:
            m = (l+r)//2
            if sorted_arr[m]<=v:
                l = m+1
            else:
                r = m
        sorted_arr.insert(l,v)




    def maxSumSubmatrix(self, matrix , k: int) -> int:

        m = len(matrix)
        n = len(matrix[0])

        ans = float('-inf')

        for u in range(m):
            arr = [0 for j in range(n)]
            for b in range(u,m):

                for j in range(n):
                    arr[j]+=matrix[b][j]

                sorted_arr = [0]
                sum_val = 0
                for r in range(n):
                    sum_val+=arr[r]
                    v = self.biSearch(sorted_arr,sum_val,k)
                    ans = max(ans,v)
                    self.biInsert(sorted_arr, sum_val)

        return ans


obj = Solution()
matrix = [[2,2,-1]]
k = 3
ans = obj.maxSumSubmatrix(matrix,k)
print(ans)


