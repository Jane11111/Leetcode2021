# -*- coding: utf-8 -*-
# @Time    : 2021-04-21 16:14
# @Author  : zxl
# @FileName: 208.py


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root_dic = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        dic = self.root_dic
        for s in word:
            if s not in dic:
                dic[s] = {}
            dic = dic[s]
        dic['end'] = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        dic = self.root_dic
        for s in word:
            if s not in dic:
                return False
            dic = dic[s]
        return 'end' in dic


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        dic = self.root_dic
        for s in prefix:
            if s not in dic:
                return False
            dic = dic[s]
        return True