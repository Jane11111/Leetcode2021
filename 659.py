# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 10:20
# @Author  : zxl
# @FileName: 659.py


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        freq_dic = {}
        for num in nums:
            if num not in freq_dic:
                freq_dic[num] = 0
            freq_dic[num] += 1

        end_dic = {}
        for idx in range(len(nums)):
            num = nums[idx]

            if freq_dic[num] == 0:
                continue

            freq_dic[num]-=1

            if num-1 in end_dic and end_dic[num-1] >0:
                if num not in end_dic:
                    end_dic[num] = 0
                end_dic[num - 1] -= 1
                end_dic[num] += 1


            elif num+1 in freq_dic and freq_dic[num+1]>0 and num+2 in freq_dic and freq_dic[num+2]>0:

                if num+2 not in end_dic:
                    end_dic[num+2] = 0
                end_dic[num+2] +=1

                freq_dic[num+1]-=1
                freq_dic[num+2] -=1
            else:
                return False


        return True







obj = Solution()
nums = [1,2,2,3,4,5]
ans = obj.isPossible(nums)
print(ans)