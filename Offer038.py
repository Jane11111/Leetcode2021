# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 15:12
# @Author  : zxl
# @FileName: Offer038.py

class Solution:


    def recursivePermutate(self,s,sub_s,used):

        if len(sub_s) == len(s):
            return [sub_s]
        dic = {}
        ans = []
        for i in range(len(used)):
            if not used[i] and s[i] not in dic:

                dic[s[i]] = True
                used[i] = True
                lst = self.recursivePermutate(s,sub_s+s[i],used)
                used[i] = False
                ans.extend(lst)
        return ans

    def permutation(self, s )  :

        used = [False for i in range(len(s))]
        ans = self.recursivePermutate(s,'',used)
        return ans

obj = Solution()
s = 'aabc'
ans = obj.permutation(s)
print(ans)





