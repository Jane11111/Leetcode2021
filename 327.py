# -*- coding: utf-8 -*-
# @Time    : 2021-07-02 14:15
# @Author  : zxl
# @FileName: 327.py


class Solution:


    def mergeSort(self,presums,i,j,tmp,lower,upper):
        if i>=j:
            return 0
        m = (i+j)//2
        n1 = self.mergeSort(presums,i,m,tmp,lower,upper)
        n2 = self.mergeSort(presums,m+1,j,tmp,lower,upper)
        n3 = self.merge(presums,i,j,m,tmp,lower,upper)
        return n1+n2+n3

    def merge(self,presums,i,j,m,tmp,lower,upper):

        ans = 0
        p = i
        l = m+1
        r = m+1
        while p<=m and l<=j:

            while l<=j and presums[l]-presums[p]<lower:
                l+=1

            while r<=j and presums[r]-presums[p]<=upper:
                r+=1
            if l<=j:
                ans+=r-l
            p+=1

        p1 = i
        p2 = m+1
        p = i
        while p<=j:
            if p1>m:
                tmp[p] = presums[p2]
                p2+=1
            elif p2>j:
                tmp[p] = presums[p1]
                p1+=1
            else:
                if presums[p1]<presums[p2]:
                    tmp[p] = presums[p1]
                    p1+=1
                else:
                    tmp[p] = presums[p2]
                    p2+=1
            p+=1
        for p in range(i,j+1):
            presums[p] = tmp[p]
        return ans



    def countRangeSum(self, nums , lower: int, upper: int) -> int:


        presums = [num for num in nums]

        for i in range(1,len(nums)):
            presums[i]+=presums[i-1]
        presums.insert(0,0)
        tmp = [0 for i in range(len(presums))]
        ans = self.mergeSort(presums,0,len(presums)-1,tmp,lower,upper)
        return ans

obj = Solution()
nums = [-2,5,-1]
lower = -2
upper = 2
ans = obj.countRangeSum(nums,lower,upper)
print(ans)




