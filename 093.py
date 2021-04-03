# -*- coding: utf-8 -*-
# @Time    : 2021-03-26 09:17
# @Author  : zxl
# @FileName: 093.py


class Solution(object):

    def isValid(self,s):

        if s[0] == '0' and len(s)>1:
            return False

        return int(s)>=0 and int(s) <= 255



    def recursiveRestore(self,s,k):
        if k == 0 and len(s) == 0:
            return ['']
        elif (k==0 and len(s) > 0) or (k>0 and len(s) == 0):
            return []
        ans = []
        for i in range(1,len(s)+1):
            sub_s = s[:i]
            if not self.isValid(sub_s):
                break
            right_str_lst = self.recursiveRestore(s[i:],k-1)
            for right_str in right_str_lst:
                if len(right_str) == 0:
                    ans.append(sub_s)
                else:
                    ans.append(sub_s+'.'+right_str)
        return ans





    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        for i in range(len(s)):
            if s[i]<'0' or s[i]>'9':
                return []

        ans = self.recursiveRestore(s,4)
        return ans

obj = Solution()
s = "010010"
ans = obj.restoreIpAddresses(s)
print(ans)

