# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 17:01
# @Author  : zxl
# @FileName: 224_2.py

class Solution:


    def recCal(self,s,m,n,arr):

        # if m == n:
        #     return int(s[m])

        st = []
        if n>m and (s[m] == '+' or s[m] == '-'):
            st.append(0)
            st.append(s[m])
            m = m+1

        snum = ''
        i = m

        while i <= n:
            if s[i].isdigit():
                snum += s[i]
                i += 1
            elif s[i] == '+' or s[i] == '-':
                st.append(int(snum))
                st.append(s[i])
                snum = ''
                i += 1

            else:
                # left = 1
                # j = i + 1
                # while j < len(s) and left != 0:
                #     if s[j] == '(':
                #         left += 1
                #     elif s[j] == ')':
                #         left -= 1
                #     j += 1
                # eq = s[i + 1:arr[i]]
                num = self.recCal(s,i+1,arr[i]-1,arr)
                snum = str(num)

                i = arr[i]+1
        if len(snum) > 0:
            st.append(int(snum))
        ans = st[0]
        for i in range(1, len(st), 2):
            if st[i] == '+':
                ans += st[i + 1]
            else:
                ans -= st[i + 1]
        return ans

    def calculate(self, s: str) -> int:

        s = s.replace(' ','')
        dic = {}
        st = []

        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
                dic[i] = i
            elif s[i] == ')':
                dic[st.pop()] = i
        ans = self.recCal(s,0,len(s)-1,dic)
        return ans




obj = Solution()
s = " 2-1 + 2 "
ans = obj.calculate(s)
print(ans)


