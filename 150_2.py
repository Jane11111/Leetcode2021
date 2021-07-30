# -*- coding: utf-8 -*-
# @Time    : 2021-07-28 19:36
# @Author  : zxl
# @FileName: 150_2.py


class Solution:
    def evalRPN(self, tokens ) -> int:


        st = []

        for c in tokens:
            if c!='+' and c!='-' and c!='*' and c!='/':
                st.append(int(c))
            else:
                n1 = st.pop()
                n2 = st.pop()
                if c == '+':
                    st.append(n1+n2)
                elif c == '-':
                    st.append(n2-n1)
                elif c == '*':
                    st.append(n1*n2)
                else:
                    st.append(int(n2/n1))
        return st[0]
obj = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
ans = obj.evalRPN(tokens)
print(ans)

