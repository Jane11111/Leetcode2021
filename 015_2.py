# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 15:00
# @Author  : zxl
# @FileName: 015_2.py

# 超时 O(N^2log(N))

class Solution(object):

    def biSearch(self,nums,s,e,k):
        if s>e:
            return False
        if s==e:
            return nums[s] == k
        if nums[s]>k or nums[e]<k:
            return False

        m = (s+e)//2
        f1 = self.biSearch(nums,s,m,k)
        f2 = self.biSearch(nums,m+1,e,k)
        return f1 or f2

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums)<3:
            return []

        nums.sort()
        dic = {}
        res = []
        for i in range(len(nums)-2):
            m = i+1
            while m<len(nums)-1:


                if (nums[i],nums[m]) in dic:
                    m+=1
                    continue
                dic[(nums[i] , nums[m])] = True  # 这样的组合已经遍历过
                # 使用二分查找
                if self.biSearch(nums,m+1,len(nums)-1,-(nums[i]+nums[m])):
                    res.append([nums[i],nums[m],-(nums[i]+nums[m])])
                    #

                m+=1

        return res

obj = Solution()
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
res = obj.threeSum(nums)
print(res)