# -*- coding: utf-8 -*-
# @Time    : 2021-04-16 16:19
# @Author  : zxl
# @FileName: 049.py


class Solution:
    def groupAnagrams(self, strs ) :
        dic = {}

        for s in strs:
            l = [c for c in s]
            l.sort()
            sorted_s = ''.join(l)
            if sorted_s in dic:
                dic[sorted_s].append(s)
            else:
                dic[sorted_s] = [s]
        ans = []
        for k in dic:
            ans.append(dic[k])
        return ans

obj = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = obj.groupAnagrams(strs)
print(ans)