# -*- coding: utf-8 -*-
# @Time    : 2021-03-26 13:22
# @Author  : zxl
# @FileName: 842.py


class Solution(object):

    def recursiveSplit(self,lst,s):

        if len(s) == 0:
            return True

        n1 = lst[-2]
        n2 = lst[-1]
        n3 = n1+n2
        if n3>2**31-1:
            return False
        s_n3 = str(n3)
        # if s_n3 == s:
        #     lst.append(n3)
        #     return True
        if s[:len(s_n3)] != s_n3:
            return False
        else:
            lst.append(n3)
            f = self.recursiveSplit(lst,s[len(s_n3):])
            if not f:
                lst.pop(-1)
            return f


    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        l = len(S)
        lst = []
        for i in range(1,l):
            s_n1 = S[:i]
            if s_n1[0] == '0' and len(s_n1)>1:
                continue
            lst.append(int(s_n1))
            for j in range(i+1,l+1):
                s_n2 = S[i:j]
                if s_n2[0] == '0' and len(s_n2) >1:
                    break
                lst.append(int(s_n2))
                f = self.recursiveSplit(lst,S[j:])
                if f and len(lst)>2:
                    return lst

                lst.pop(-1)
            lst.pop(-1)
        return lst

obj = Solution()
s = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
ans = obj.splitIntoFibonacci(s)
print(ans)




