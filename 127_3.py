# -*- coding: utf-8 -*-
# @Time    : 2021-06-26 11:46
# @Author  : zxl
# @FileName: 127_3.py


# 虚拟节点 + 双向广度优先搜索


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
                vnode = word[:i] + '*' + word[i + 1:]
                vlst.append(vnode)
            if word not in w2v:
                w2v[word] = {}
            for vnode in vlst:
                if vnode not in v2w:
                    v2w[vnode] = {}
                v2w[vnode][word] = True
                w2v[word][vnode] = True
        dis_begin = {beginWord:1}
        dis_end = {endWord:1}

        step = 1

        begin_lst = [beginWord]
        end_lst = [endWord]


        # TODO 如果存在一条路径，那么在找到这条路径之前，两个list一定不会有任何一个变成空
        while len(begin_lst)>0 and len(end_lst)>0: # TODO 为什么可以用and

            l = len(begin_lst)

            while l:
                s = begin_lst.pop(0)
                l-=1
                if s in dis_end:
                    return (dis_begin[s]+dis_end[s]-1)

                for vnode in w2v[s]:
                    for word in v2w[vnode]:
                        if word not in dis_begin:
                            begin_lst.append(word)
                            dis_begin[word] = step+1

            l = len(end_lst)
            while l:
                s = end_lst.pop(0)
                l -= 1
                if s in dis_begin:
                    return (dis_begin[s]+dis_end[s]-1)

                for vnode in w2v[s]:
                    for word in v2w[vnode]:
                        if word not in dis_end:
                            end_lst.append(word)
                            dis_end[word] = step+1



            step +=1
        return 0


