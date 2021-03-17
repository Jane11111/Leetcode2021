# -*- coding: utf-8 -*-
# @Time    : 2021-03-12 15:17
# @Author  : zxl
# @FileName: 113.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """

        if root == None :
            return []
        if not root.left and not root.right:
            if root.val == targetSum:
                return [[targetSum]]
            else:
                return []

        ans = []
        lst1 = self.pathSum(root.left,targetSum-root.val)
        lst2 = self.pathSum(root.right,targetSum-root.val)
        lst1.extend(lst2)

        for lst in lst1 :
            lst.insert(0,root.val)
            ans.append(lst)
        return ans

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
targetSum = 3
ans = obj.pathSum(root,targetSum)
print(ans)
