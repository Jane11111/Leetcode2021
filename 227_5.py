# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 19:45
# @Author  : zxl
# @FileName: 227_5.py



class Solution:

    def calculate(self, s: str) -> int:

        s = s.replace(' ','')
        i = 0

        while i<len(s) and s[i].isdigit():
            i+=1

        st = [int(s[:i])]

        while i<len(s):
            op = s[i]
            j = i+1
            while j<len(s) and s[j].isdigit():
                j+=1
            if op == '+' or op == '-':
                st.append(op)
                st.append(int(s[i+1:j]))
            else:
                cur_num = int(s[i+1:j])

                if op == '*':
                    st[-1] *= cur_num
                else:
                    st[-1] //= cur_num

            i = j
        ans = st[0]
        for i in range(1,len(st),2):
            if st[i] == '+':
                ans+= st[i+1]
            else:
                ans-= st[i+1]
        return ans

