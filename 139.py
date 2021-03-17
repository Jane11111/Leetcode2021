# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 15:52
# @Author  : zxl
# @FileName: 139.py

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        m = len(s)
        arr = []
        for i in range(m):
            arr.append([False for i in range(m)])

        for i in range(m):
            if s[i] in wordDict:
                arr[i][i] = True

        for l in range(1, m + 1): #字符串长度
            for i in range(m):

                j = i+l-1
                if j>=m:
                    break
                f = s[i:j+1] in wordDict
                for k in range(i,j):
                    if arr[i][k] and arr[k+1][j]:
                        f = True
                        break
                arr[i][j] = f
        return arr[0][m-1]

obj = Solution()
s="catsandog"
wordDict =  ["cats","dog","sand","and","cat"]
ans = obj.wordBreak(s,wordDict)
print(ans)
