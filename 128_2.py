# -*- coding: utf-8 -*-
# @Time    : 2021-05-16 21:30
# @Author  : zxl
# @FileName: 128_2.py




class Solution:
    def longestConsecutive(self, nums ) -> int:


        dic = {}
        for num in nums:
            dic[num] = True

        ans = 0
        visited= {}
        for num in nums:
            if num in visited: #避免最小数字重复的情况
                continue
            visited[num ] = True
            if num-1 in dic:
                continue
            else: #只有是最小的数，才开始遍历
                count = 1
                cur_num = num+1
                while cur_num in dic:
                    cur_num +=1
                    count+=1
                ans = max(ans,count)
        return ans

