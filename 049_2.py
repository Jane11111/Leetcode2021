# -*- coding: utf-8 -*-
# @Time    : 2021-05-13 16:05
# @Author  : zxl
# @FileName: 049_2.py


class Solution:
    def groupAnagrams(self, strs )  :


        dic = {}
        for s in strs:
            l = [c for c in s]
            l.sort()
            new_s = ''.join(l)
            if new_s not in dic:
                dic[new_s] = []
            dic[new_s].append(s)
        ans = []
        for k in dic:
            ans.append(dic[k])
        return ans



obj = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = obj.groupAnagrams(strs)
print(ans)