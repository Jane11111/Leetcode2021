# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 19:06
# @Author  : zxl
# @FileName: 224_3.py



class Solution:

    def calculate(self, s: str) -> int:

        s = s.replace(' ','')


        st = [1]
        cur_op = 1

        lst = []
        snum = '0'
        for i in range(len(s)):

            if s[i] == '+' or s[i] == '-':
                lst.append(int(snum))

                if st[-1] == 1:
                    if s[i] == '+':
                        lst.append('+')
                        cur_op = 1
                    else:
                        lst.append('-')
                        cur_op = -1
                else:
                    if s[i] == '+':
                        lst.append('-')
                        cur_op = -1
                    else:
                        lst.append('+')
                        cur_op = 1
                snum= '0'
            elif s[i] == '(':
                st.append(cur_op) # 将当前的operation入栈
            elif s[i] == ')':
                st.pop() # 将当前operation出栈
            else:
                snum+= s[i]

        # if len(snum)>0:
        lst.append(int(snum))

        ans = lst[0]
        for i in range(1,len(lst),2):
            if lst[i] == '+':
                ans+=lst[i+1]
            else:
                ans-=lst[i+1]
        return ans

obj = Solution()
s = "(1-(4+5+2)-3)+(6+8)"
ans = obj.calculate(s)
print(ans)



