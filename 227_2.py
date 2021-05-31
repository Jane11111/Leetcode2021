# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 21:52
# @Author  : zxl
# @FileName: 227_2.py



class Solution:
    def calculate(self, s: str) -> int:


        s = s.replace(' ','')
        if len(s) == 0:
            return 0

        st = []

        num = ''
        i = 0
        while i<len(s):
            if s[i]>='0' and s[i]<='9':
                num += s[i]
                i+=1
            elif s[i] == '+' or s[i] == '-':
                if len(num)>0:
                    st.append(int(num))
                st.append(s[i])
                num = ''
                i+=1
            else:
                if len(num)>0:
                    st.append(int(num))


                op = s[i]
                i+=1
                num = ''
                while i<len(s) and s[i]>='0' and s[i]<='9':
                    num+=s[i]
                    i+=1
                num1 = st.pop()
                num2 = int(num)
                if op == '*':
                    st.append(num1*num2)
                else:
                    st.append(num1//num2)
                num = ''


        if len(num)>0:
            st.append(int(num))
        ans = st[0]

        for i in range(1,len(st),2):
            if st[i] == '+':
                ans += st[i+1]
            else:
                ans -= st[i+1]
        return ans



obj = Solution()
s = "0"
ans = obj.calculate(s)
print(ans)