# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 17:34
# @Author  : zxl
# @FileName: 454.py


class Solution:

    def two_sum(self,nums1,nums2):
        dic = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                v = nums1[i]+nums2[j]
                if v not in dic:
                    dic[v] = 0
                dic[v]+=1
        return dic


    def fourSumCount(self, nums1 , nums2 , nums3 , nums4 ) -> int:

        dic1 = self.two_sum(nums1,nums2)
        dic2 = self.two_sum(nums3,nums4)

        count = 0
        for k in dic1:
            if -k in dic2:
                count+=(dic1[k]*dic2[-k])
        return count






A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
obj = Solution()
ans = obj.fourSumCount(A,B,C,D)
print(ans)