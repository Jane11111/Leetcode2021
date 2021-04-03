# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 14:01
# @Author  : zxl
# @FileName: 316.py


#TODO 超时

class Solution(object):

    def recursiveFind(self,s,dic):
        if len(s) == 0:
            return ''
        if dic[s[0]] == 1: # 这个字母频率为1，必须留着
            return s[0] + self.recursiveFind(s[1:],dic)
        elif dic[s[0]] > 1: # 这个字母频率很高，可以留着，也可以删除

            if len(s) == 1:
                return ''

            dic[s[0]] -=1
            s2 = self.recursiveFind(s[1:],dic)
            dic[s[0]] += 1
            if s2[0] < s[0] or s[0] == s[1]:
                return s2

            num = dic[s[0]]
            dic[s[0]] = 0
            s1 = s[0] + self.recursiveFind(s[1:], dic)
            dic[s[0]] = num

            if s1<s2:
                return s1
            else:
                return s2
        else: # dic[s[0]] == 0 前面留过这个字母，需要都删了
            return self.recursiveFind(s[1:],dic)

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 0
            dic[s[i]] += 1
        ans = self.recursiveFind(s,dic)
        return ans

obj = Solution()
s = "bxshkpdwcsjdbikywvioxrypfzfbppydfilfxxtouzzjxaymjpmdoevv"
ans = obj.removeDuplicateLetters(s)
print(ans)