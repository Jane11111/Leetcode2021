# -*- coding: utf-8 -*-
# @Time    : 2021-04-21 17:47
# @Author  : zxl
# @FileName: 212_2.py


# TODO 这个复杂度其实也跟words长度有关，words长度小的话，就及时停止了

class TreeNode():

    def __init__(self,val,is_end ,child ):
        self.val = val
        self.is_end = is_end
        self.child = child



class TrieTree():

    def __init__(self):
        self.root = TreeNode('',False,{})

    def insert(self,word):

        cur_root = self.root
        for c in word:
            if c not in cur_root.child:
                cur_root.child[c] = TreeNode(c,False,{})
            cur_root = cur_root.child[c]
        cur_root.is_end = True
        cur_root.val = word







class Solution:


    def find(self,board,visited,root,i,j,result):
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or visited[i][j] :
            return



        c = board[i][j]
        if c not in root.child:
            return

        if root.child[c].is_end :
            result.append(root.child[c].val)
            root.child[c].is_end = False

        cur_root = root.child[c]

        visited[i][j] = True
        self.find(board,visited,cur_root,i+1,j,result)
        self.find(board, visited, cur_root, i  , j+1, result)
        self.find(board, visited, cur_root, i-1, j, result)
        self.find(board, visited, cur_root, i  , j-1, result)


        visited[i][j] = False

    def findWords(self, board, words):

        my_tree = TrieTree()

        for word in words:
            my_tree.insert(word)

        m = len(board)
        n = len(board[0])
        visited = []
        for i in range(m):
            visited.append([False for j in range(n)])
        result = []
        for i in range(m):
            for j in range(n):
                self.find(board,visited,my_tree.root,i,j,result)
        return result

obj = Solution()
boards = [["a","a"]]
words = ["aaa"]
ans = obj.findWords(boards,words)
print(ans)