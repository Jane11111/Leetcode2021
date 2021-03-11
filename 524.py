# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 20:34
# @Author  : zxl
# @FileName: 524.py


class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        ans = ""
        for item in dictionary:

            i = 0
            j = 0
            while i<len(item) and j<len(s):

                while j<len(s) and s[j] != item[i]:
                    j+=1
                if j<len(s) and item[i] == s[j]:
                    i+=1
                j +=1

            if i == len(item):
                if len(item) > len(ans):
                    ans = item
                elif len(item) == len(ans) and item<ans:
                    ans = item
        return ans

obj = Solution()
s="abpcplea"
d = ["ale","apple","monkey","plea", "abpcplaaa","abpcllllll","abccclllpppeeaaaa"]
ans = obj.findLongestWord(s,d)
print(ans)

