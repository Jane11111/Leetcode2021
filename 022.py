# -*- coding: utf-8 -*-
# @Time    : 2021-03-25 13:55
# @Author  : zxl
# @FileName: 022.py


class Solution(object):





    def recursiveGen(self,l_n,r_n,origin_s):
        if l_n == 0 and r_n == 0:
            return ['']
        elif l_n == 0:
            ans = ''
            for i in range(r_n):
                ans += ')'
            return [ans]
        elif r_n == 0:
            ans = ''
            for i in range(l_n):
                ans+='('
            return [ans]
        else:
            ans = []
            if len(origin_s) == 0:
                lst1 = self.recursiveGen(l_n-1,r_n,'(')
                for item in lst1:
                    ans.append('('+item)
            else:
                lst1 = self.recursiveGen(l_n-1,r_n,origin_s+'(')
                lst2 = self.recursiveGen(l_n,r_n-1,origin_s[:-1])
                for item in lst1:
                    ans.append('('+item)
                for item in lst2:
                    ans.append(')'+item)
            return ans





    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = self.recursiveGen(n,n,'')
        return ans

obj = Solution()
n = 3
ans = obj.generateParenthesis(n)
print(ans)


