# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 16:24
# @Author  : zxl
# @FileName: 018.py





class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        res = []


        for i in range(len(nums)-3):

            # if nums[i] > target :
            #     break

            if i>0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            # if nums[i]+nums[j]>target:
            #     break

            while j<len(nums)-2:


                m = j+1
                n = len(nums)-1

                while m<n:
                    if nums[m]+nums[n]>target-(nums[i]+nums[j]):
                        n-=1
                    elif nums[m]+nums[n]<target-(nums[i]+nums[j]):
                        m+=1
                    else:
                        res.append([nums[i],nums[j],nums[m],nums[n]])
                        m+=1
                        n-=1
                        while m<n and nums[m]==nums[m-1]:
                            m+=1
                        while m<n and nums[n] == nums[n+1]:
                            n-=1
                j+=1
                while j<len(nums)-2 and nums[j] == nums[j-1]:
                    j+=1

        return res
obj = Solution()
nums = [1,-2,-5,-4,-3,3,3,5]
target = -11
res = obj.fourSum(nums,target)
print(res)



