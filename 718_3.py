# -*- coding: utf-8 -*-
# @Time    : 2021-05-24 16:12
# @Author  : zxl
# @FileName: 718_3.py



class Solution:
    def findLength(self, nums1 , nums2 ) -> int:

        m = len(nums1)
        n = len(nums2)
        ans = 0
        for i in range(m+n):
            end1 = min(i,m-1)
            start1 = max(0,i-n+1)

            end2 = n - max(1,(i-m+2))

            l = end1-start1+1
            count = 0
            j = 0
            while j<l :
                if nums1[end1 - j] != nums2[end2 - j]:
                    ans = max(ans,count)
                    count = 0
                else:
                    count+=1
                j+=1
            ans = max(ans,count)
        return ans


obj = Solution()

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]

ans = obj.findLength(nums1,nums2)
print(ans)