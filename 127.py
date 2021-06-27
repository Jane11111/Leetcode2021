# -*- coding: utf-8 -*-
# @Time    : 2021-06-26 10:54
# @Author  : zxl
# @FileName: 127.py



class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList ) -> int:

        if endWord not in wordList:
            return 0

        valided_dic = {item:True for item in wordList} # TODO 用字典不会超时

        lst = [beginWord]
        visited = {beginWord:True}
        step = 1
        char_lst = [chr(ord('a')+i) for i in range(26)]
        while len(lst)>0:
            l = len(lst)

            while l:
                l-=1
                s = lst.pop(0)
                if s == endWord:
                    return step
                for i in range(len(s)):
                    for c in char_lst:
                        if s[i] == c:
                            continue
                        new_s = s[:i]+c+s[i+1:]
                        if new_s in valided_dic and new_s not in visited:
                            lst.append(new_s)
                            visited[new_s] = True
            step+=1


        return 0

