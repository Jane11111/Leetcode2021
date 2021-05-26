# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 14:52
# @Author  : zxl
# @FileName: 726_2.py



class Solution:
    def countOfAtoms(self, formula: str) -> str:


        st = []
        dic = {}

        i = len(formula)-1
        count = ''
        atom = ''
        while i>=0:

            if formula[i]>='0' and formula[i]<='9':
                count = formula[i]+count
            elif formula[i]>='a' and formula[i]<='z':
                atom = formula[i]+atom
            elif formula[i]>='A' and formula[i]<='Z':
                atom  = formula[i]+atom
                if atom not in dic:
                    dic[atom] = 0
                if len(count) == 0:
                    count = '1'
                count = int(count)
                if len(st)>0:
                    count*=st[-1]
                dic[atom] += count
                atom = ''
                count = ''
            elif formula[i] == ')':
                if len(count) == 0:
                    count = '1'
                count = int(count)
                if len(st) >0:
                    count *= st[-1]

                st.append(count)
                count = ''
            else:
                st.pop()
            i-=1
        lst = [[x, y] for x, y in dic.items()]
        lst.sort()
        ans = ''
        for atom, count in lst:
            ans += atom
            if count > 1:
                ans += str(count)
        return ans

obj = Solution()
formula = 'Mg(OH)2'
ans = obj.countOfAtoms(formula)
print(ans)








