# -*- coding: utf-8 -*-
# @Time    : 2021-08-09 19:17
# @Author  : zxl
# @FileName: Ali002.py



import sys

class TreeNode:

    def __init__(self,val,left= None,right=None):
        self.val = val

        self.left = left
        self.right =right

def findDepth(root,thres):

    if not root:
        return 0,0,True

    l1,l2,lf = findDepth(root.left,thres)
    r1,r2,rf = findDepth(root.right,thres)

    if not lf or not rf:
        return -1,-1,False

    l = l1+1
    r = r2+1
    if abs(l-r) > thres:
        return -1,-1,False
    return l,r,True

def solve(arr,n):
    root = TreeNode(arr[0])
    thres = min(11,n//2)

    for i in range(1,n):

        num = arr[i]
        cur_p = TreeNode(num)

        p = root
        while True:
            if num<p.val:
                if p.left == None:
                    p.left = cur_p
                    break
                else:
                    p = p.left
            else:
                if p.right == None:
                    p.right = cur_p
                    break
                else:
                    p = p.right
    n1,n2,f = findDepth(root,thres)
    return f




if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    while T:

        N = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        arr = list(map(int, line.split()))
        ans = solve(arr,N)
        if ans:
            print('YES')
        else:
            print('NO')


        T-=1

