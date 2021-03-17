# -*- coding: utf-8 -*-
# @Time    : 2021-03-12 14:45
# @Author  : zxl
# @FileName: 105_2.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def recursiveConstruct(self,preorder,s1,e1,inorder,s2,e2):
        if s1>e1:
            return None

        count = 0
        while inorder[s2+count] != preorder[s1]:
            count += 1
        head = TreeNode(preorder[s1])
        head.left = self.recursiveConstruct(preorder,s1+1,s1+count, inorder, s2,s2+count-1)
        head.right = self.recursiveConstruct(preorder,s1+count+1,e1,inorder,s2+count+1,e2)
        return head



    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        head = self.recursiveConstruct(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
        return head

obj = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

head = obj.buildTree(preorder,inorder)
print(head)