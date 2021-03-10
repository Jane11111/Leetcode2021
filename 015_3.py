# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 15:10
# @Author  : zxl
# @FileName: 015_3.py

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
            if nums[i] > 0:
                break
            if i>0 and i<len(nums)-2 and nums[i] == nums[i-1]:
                continue

            m = i+1
            n = len(nums)-1
            target = -nums[i]

            while m<n:
                # if (nums[i], nums[m]) in dic:
                #     m+=1
                #     continue
                if nums[m] + nums[n]> target:
                    # dic[(nums[i], nums[m])] = True
                    n-=1
                elif nums[m]+nums[n]<target:
                    # dic[(nums[i], nums[m])] = True
                    m+=1
                else:
                    if (nums[i],nums[m]) not in dic:
                        # dic[(nums[i],nums[m])] = True
                        res.append([nums[i],nums[m],nums[n]])
                    m += 1
                    n -= 1
                    while m<n and nums[m] == nums[m-1]:
                        m+=1
                    while n>m and nums[n] == nums[n+1]:
                        n-=1



        return res

obj = Solution()
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
res = obj.threeSum(nums)
print(res)