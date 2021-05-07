# -*- coding: utf-8 -*-
# @Time    : 2021-05-06 15:32
# @Author  : zxl
# @FileName: 1630.py


class Solution:
    def checkArithmeticSubarrays(self, nums , l , r )  :

        ans = []

        for i in range(len(l)):
            new_lst = nums[l[i]:r[i]+1]

            new_lst.sort()
            f = True
            for j in range(1,len(new_lst)):
                if new_lst[j]-new_lst[j-1]!=new_lst[1]-new_lst[0]:
                    f = False
                    break
            ans.append(f)
        return ans




nums=[4,6,5,9,3,7]
l=[0,0,2]
r=[2,3,5]
obj = Solution()
ans = obj.checkArithmeticSubarrays(nums,l,r)
print(ans)