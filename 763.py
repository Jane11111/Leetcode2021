# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 22:10
# @Author  : zxl
# @FileName: 763.py


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        dic = {}
        for i in range(len(S)):
            dic[S[i]] = i

        ans = []

        i = 0
        while i<len(S):
            idx = dic[S[i]]
            j = i+1
            while j<=idx:
                idx = max(idx,dic[S[j]])
                j+=1
            ans.append(j-i)
            i=j
        return ans

obj = Solution()
S = "ababcbacadefegdehijhklij"
ans = obj.partitionLabels(S)
print(ans)

