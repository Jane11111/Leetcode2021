# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 16:06
# @Author  : zxl
# @FileName: 139_2.py

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        m = len(s)
        arr = [False for i in range(m)]
        arr[0] = s[0] in wordDict

        for i in range(1,m):
            if s[:i+1]  in wordDict:
                arr[i] = True
                continue
            for j in range(0,i):
                if arr[j] and s[j+1:i+1] in wordDict:
                    arr[i] = True
                    break
        return arr[m-1]


obj = Solution()
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
ans = obj.wordBreak(s,wordDict)
print(ans)