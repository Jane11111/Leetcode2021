# -*- coding: utf-8 -*-
# @Time    : 2021-05-13 20:30
# @Author  : zxl
# @FileName: 492.py



class Solution:


    def findSubsequences(self, nums  ) :


        lst = [[]]


        for num in nums:
            for k in range(len(lst)):
                if len(lst[k]) == 0 or  lst[k][-1] <=num:
                    tmp = lst[k].copy()
                    tmp.append(num)
                    lst.append(tmp)

        dic = {}
        ans = []
        for item in lst:
            if len(item)>=2:
                str_lst = [str(i) for i in item]
                s = ','.join(str_lst)
                if s not in dic:
                    ans.append(item)
                dic[s] = True
        return ans

obj = Solution()
nums = [4,6,7,7]
ans = obj.findSubsequences(nums)
print(ans)






