# -*- coding: utf-8 -*-
# @Time    : 2021-08-01 13:06
# @Author  : zxl
# @FileName: 127_4.py


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList ) -> int:



        dic = {}

        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(len(word)):
                newword = word[:j]+'*'+word[j+1:]
                if newword not in dic:
                    dic[newword] = []
                dic[newword].append(word)

        lst = [beginWord]

        visited = {}
        visited[beginWord] = True
        step = 0

        while len(lst) >0:
            l = len(lst)
            step+=1

            while l:
                l-=1
                word = lst.pop(0)
                if word == endWord:
                    return step

                for j in range(len(word)):
                    newword = word[:j]+'*'+word[j+1:]
                    if newword in dic:
                        for tmp in dic[newword]: # 距离当前word相差1的词
                            if tmp not in visited or not visited[tmp]:
                                visited[tmp]= True
                                lst.append(tmp)

        return 0


