# -*- coding: utf-8 -*-
# @Time    : 2021-04-21 16:57
# @Author  : zxl
# @FileName: 211.py


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root_dic = {}


    def addWord(self, word: str) -> None:
        dic = self.root_dic
        for s in word:
            if s not in dic:
                dic[s] = {}
            dic = dic[s]
        dic['end'] =True


    def search(self, word: str) -> bool:

        dic_lst = [self.root_dic]
        for s in word:
            if s == '.':
                l = len(dic_lst)
                i = 0
                while i<l:
                    cur_dic = dic_lst.pop(0)
                    for k in cur_dic:
                        if k != 'end':
                            dic_lst.append(cur_dic[k])
                    i+=1
            else:
                l = len(dic_lst)
                i = 0
                while i<l:
                    cur_dic = dic_lst.pop(0)
                    if s in cur_dic:
                        dic_lst.append(cur_dic[s])
                    i+=1
        for dic in dic_lst:
            if 'end' in dic:
                return True
        return False

