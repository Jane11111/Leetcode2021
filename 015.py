# -*- coding: utf-8 -*-
# @Time    : 2021-03-04 21:27
# @Author  : zxl
# @FileName: 015.py

# 超时 O(N^3)

class Solution(object):
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

                n = len(nums)-1

                if (nums[i],nums[m]) in dic:
                    m+=1
                    continue
                dic[(nums[i] , nums[m])] = True  # 这样的组合已经遍历过
                while n>m and nums[n] > -(nums[i] + nums[m]):
                    n-=1

                if n>m and nums[n] == -(nums[i]+nums[m]):
                    res.append([nums[i],nums[m],nums[n]])
                    #

                m+=1

        return res

obj = Solution()
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
res = obj.threeSum(nums)
print(res)











