# -*- coding: utf-8 -*-
# @Time    : 2021-06-26 12:04
# @Author  : zxl
# @FileName: 126.py

import copy
class Solution:

    def constructDic(self,wordList):
        w2v = {}
        v2w = {}
        for word in wordList:
            if word not in w2v:
                w2v[word] = {}

            vlst = []
            for i in range(len(word)):
                s = word[:i] + '*' + word[i + 1:]
                vlst.append(s)
            for vnode in vlst:
                if vnode not in v2w:
                    v2w[vnode] = {}
                v2w[vnode][word] = True
                w2v[word][vnode] = True
        return w2v, v2w
    def constructPath(self,beginWord,curWord,pre,lst):

        for sub_lst in lst:
            sub_lst.insert(0,curWord)

        if curWord == beginWord:
            return lst

        ans = []
        for pre_word in pre[curWord]:
            old_lst = copy.deepcopy(lst)
            cur_ans = self.constructPath(beginWord,pre_word,pre,old_lst)
            ans.extend(cur_ans)
        return ans


    def findLadders(self, beginWord: str, endWord: str, wordList ) :

        if endWord not in wordList:
            return []

        wordList.append(beginWord)

        w2v, v2w = self.constructDic(wordList)

        pre = {beginWord:[]}
        lst = [beginWord]
        visited = {beginWord:True}
        found = False

        while len(lst)>0 and not found:

            l = len(lst)
            tmp = []
            while l:
                s = lst.pop(0)
                l-=1


                for vnode in w2v[s]:
                    for word in v2w[vnode]:
                        if word not in visited : # 之前没有被visited
                            # visited[word] = True
                            tmp.append(word)
                            if word not in pre:
                                pre[word] = []
                            pre[word].append(s)
                            if word == endWord: # 当前这一轮只要能够得到endWord，仍然合法
                                found = True
            for word in tmp:
                if word not in visited:
                    visited[word] =True
                    lst.append(word)


        if not found :
            return []


        ans = self.constructPath(beginWord,endWord,pre,[[]])
        return ans




