# -*- coding: utf-8 -*-
# @Time    : 2021-05-13 22:19
# @Author  : zxl
# @FileName: NC91.py



class Solution:

    def biSearch(self,nums,target):

        if len(nums) == 0 or target>nums[-1]:
            return len(nums)

        lo = 0
        hi = len(nums)-1
        while lo<hi:
            m = (lo+hi)//2
            if nums[m]<target:
                lo = m+1
            else:
                hi = m
        return lo


    def LIS(self , arr ):


        vec = []
        maxlen_lst = []
        for i in range(len(arr)):
            idx = self.biSearch(vec,arr[i])
            if idx == len(vec):
                vec.append(arr[i])
            else:
                vec[idx] = arr[i]
            maxlen_lst.append(idx+1)


        j = len(vec)
        for i in range(len(arr)-1,-1,-1):
            if  maxlen_lst[i] == j:
                j-=1
                vec[j] = arr[i]

        return vec


obj = Solution()
arr = [2,1,5,3,6,4,8,9,7]
ans = obj.LIS(arr)
print(ans)