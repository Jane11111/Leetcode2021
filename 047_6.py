# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 14:43
# @Author  : zxl
# @FileName: 047_6.py



class Solution:
    def permuteUnique(self, nums ) :

        nums.sort()
        ans = [[]]
        n = len(nums)

        for i in range(n):# 一共有n个number，一次排放
            new_ans = []

            for lst in ans: # 当前这个lst下一个怎么放
                j = 0
                while j<len(nums): # idx
                    if j not in lst:

                        tmp = [item for item in lst]
                        tmp.append(j)
                        # new_ans.append(tmp)
                        j+=1
                        while j<len(nums) and nums[j] == nums[j-1]:
                            j+=1
                        new_ans.append(tmp)
                    else:
                        j+=1
            ans = new_ans
        for i in range(len(ans)):

            ans[i] = [nums[idx] for idx in ans[i]]


        return ans




