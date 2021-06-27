# -*- coding: utf-8 -*-
# @Time    : 2021-06-25 17:08
# @Author  : zxl
# @FileName: 433+2.py


# BFS
class Solution:


    def minMutation(self, start: str, end: str, bank ) -> int:


        st = [start]
        visited = {start :True}
        step = 0
        valid = {item: True for item in bank}

        while len(st)>0:
            l = len(st)

            while l:# 这一层遍历完
                cur_s = st.pop(0)
                if cur_s == end:
                    return step
                l-=1

                for i in range(len(cur_s)):

                    for c in ['A','T','C','G']:
                        if c == cur_s[i]:
                            continue
                        new_s = cur_s[:i]+c+cur_s[i+1:]
                        if new_s in visited or new_s not in valid:
                            continue

                        st.append(new_s)
                        visited[new_s] = True


            step +=1



        return -1
