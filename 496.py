# -*- coding: utf-8 -*-
# @Time    : 2021-04-03 10:27
# @Author  : zxl
# @FileName: 496.py


class Solution:
    def nextGreaterElement(self, nums1, nums2):

        n = len(nums2)

        lst = []
        arr = [-1 for i in range(n)]

        for i in range(n):

            if len(lst) == 0 or nums2[i]<=nums2[lst[-1]]:
                lst.append(i)
            else:

                while len(lst) > 0 and nums2[i] > nums2[lst[-1]]:
                    arr[lst[-1]] = nums2[i]
                    lst.pop()
                lst.append(i)
        dic = {}
        for i in range(n):
            dic[nums2[i]] = i

        ans = []
        for i in range(len(nums1)):
            idx = dic[nums1[i]]
            bigger_val = arr[idx]
            ans.append(bigger_val)
        return ans

obj = Solution()
nums1 = [2,4]
nums2 = [1,2,3,4]
ans = obj.nextGreaterElement(nums1,nums2)
print(ans)

