# -*- coding: utf-8 -*-
# @Time    : 2021-06-02 13:47
# @Author  : zxl
# @FileName: 227_3.py



class Solution:
    def calculate(self, s: str) -> int:

        st = []
        s = s.replace(' ','')

        i = 0
        while i<len(s):
            if s[i].isdigit():
                j = i+1
                while j<len(s) and s[j].isdigit():
                    j+=1
                st.append(int(s[i:j]))
                i = j
            elif s[i] == '+' or s[i] == '-':
                st.append(s[i])
                i+=1
            else:
                j = i+1
                while j<len(s) and s[j].isdigit():
                    j+=1
                num2 = int(s[i+1:j])
                num1 = st.pop()
                if s[i] == '*':
                    st.append(num1*num2)
                else:
                    st.append(num1//num2)

                i = j
        num = st[0]
        for i in range(1,len(st),2):
            if st[i] == '+':
                num+=st[i+1]
            else:
                num-=st[i+1]
        return num
