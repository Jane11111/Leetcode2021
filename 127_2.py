# -*- coding: utf-8 -*-
# @Time    : 2021-06-26 11:05
# @Author  : zxl
# @FileName: 127_2.py

# 虚拟节点


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList ) -> int:

        if endWord not in wordList:
            return 0

        v2w = {}
        w2v = {}

        wordList.append(beginWord)
        for word in wordList:

            vlst = []
            for i in range(len(word)):
                vnode = word[:i]+'*'+word[i+1:]
                vlst.append(vnode)
            if word not in w2v:
                w2v[word] = {}
            for vnode in vlst:
                if vnode not in v2w:
                    v2w[vnode] = {}
                v2w[vnode][word] = True
                w2v[word][vnode] = True

        step = 1
        lst = [beginWord]
        visited = {beginWord:True}

        while len(lst)>0:
            l = len(lst)

            while l:
                l-=1
                s = lst.pop(0)
                if s == endWord:
                    return step
                vlst = w2v[s]
                for vnode in vlst:
                    for word in v2w[vnode]:
                        if word not in visited:
                            lst.append(word)
                            visited[word] =True
            step +=1
        return step

obj =Solution()
beginWord = 'hot'
endWord = 'dog'
wordList = ['hot','dog']
ans = obj.ladderLength(beginWord,endWord,wordList)
print(ans)
