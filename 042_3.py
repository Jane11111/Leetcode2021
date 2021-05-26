# -*- coding: utf-8 -*-
# @Time    : 2021-05-17 22:19
# @Author  : zxl
# @FileName: 042_3.py




class Solution(object):




    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        st = []
        ans = 0
        for i in range(len(height)):
            while len(st)>0 and height[i]>height[st[-1]]:
                top = st.pop()
                if len(st)>0:
                    left = st[-1]
                    width = i-left-1
                    height = min(height[left],height[i])-height[top]
                    ans += width*height
            st.append(i)
        return ans
