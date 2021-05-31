# -*- coding: utf-8 -*-
# @Time    : 2021-05-30 21:39
# @Author  : zxl
# @FileName: 432.py


class DoubleNode():

    def __init__(self,key,val,left=None,right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.node_dic = {}
        self.pre_value_dic = {}
        self.post_value_dic = {}
        self.head = DoubleNode('',-1) #dummy node
        self.tail = DoubleNode('',-1)
        self.head.right = self.tail
        self.tail.left = self.head

    def insertNewNode(self,p):

        #插入的node一定value是1

        pre = self.tail.left
        pre.right = p
        p.left = pre
        p.right = self.tail
        self.tail.left = p

        if 1 not in self.pre_value_dic:
            self.pre_value_dic[1] = p
            self.post_value_dic[1] = p
        else:
            self.post_value_dic[1] = p

    def updateValueDic(self,p,num):
        pre = p.left
        post = p.right

        if self.pre_value_dic[p.val+num] == p and self.post_value_dic[p.val+num] == p:
            self.pre_value_dic.pop(p.val+num)
            self.post_value_dic.pop(p.val+num)
        elif self.pre_value_dic[p.val+num] == p:
            self.pre_value_dic[p.val+num] = post
        elif self.post_value_dic[p.val+num] == p:
            self.post_value_dic[p.val+num] = pre

    def deleteNode(self,p):

        self.node_dic.pop(p.key)

        pre = p.left
        post = p.right
        self.updateValueDic(p,0)

        pre.right = post
        post.left = pre




    def updateNodeLeft(self,p):

        val = p.val

        p.val += 1



        if val+1  in self.pre_value_dic:

            self.updateValueDic(p, -1)  # 旧的value字典

            pre = self.pre_value_dic[val+1]


            p.left.right = p.right
            p.right.left = p.left


            p.left = pre.left
            pre.left.right = p

            p.right = pre
            pre.left = p

            # tmp = self.head
            # while tmp:
            #     print(tmp.key, tmp.val)
            #     tmp = tmp.right

            # if self.pre_value_dic[val+1] == self.post_value_dic[val+1]:
            #     self.post_value_dic[val+1] = p
            self.pre_value_dic[val+1] = p #新的value字典

        else:

            # tmp = self.head
            # while tmp:
            #     print(tmp.key, tmp.val)
            #     tmp = tmp.right
            # for k in self.pre_value_dic:
            #     print(k,self.pre_value_dic[k].key,self.pre_value_dic[k].val)

            if self.pre_value_dic[val] != p:
                # if self.post_value_dic[val] == p:
                #     self.post_value_dic[val] = p.left
                pre = self.pre_value_dic[val]

                self.updateValueDic(p, -1)

                p.left.right = p.right
                p.right.left = p.left


                p.left = pre.left
                pre.left.right = p

                p.right = pre
                pre.left = p
            else:
                self.updateValueDic(p,-1)


            self.pre_value_dic[val+1] = p # 新的value字典
            self.post_value_dic[val+1] = p
        # tmp = self.head
        # while tmp:
        #     print(tmp.key, tmp.val)
        #     tmp = tmp.right




    def updateNodeRight(self,p):


        val = p.val

        # tmp = self.head
        # while tmp:
        #     print(tmp.key, tmp.val, '----', tmp.left.key if tmp.left else 'None',
        #           tmp.right.key if tmp.right else 'None')
        #     tmp = tmp.right


        if p.val == 1:
            self.deleteNode(p)


        else:
            p.val-=1
            if val-1 in self.post_value_dic:

                # tmp = self.head
                # while tmp:
                #     print(tmp.key, tmp.val)
                #     tmp = tmp.right
                # for k in self.pre_value_dic:
                #     print(k,self.pre_value_dic[k].key,self.pre_value_dic[k].val)

                self.updateValueDic(p, 1)  # 旧的value字典
                post = self.post_value_dic[val-1] # node位置改变

                p.left.right = p.right
                p.right.left = p.left

                p.right = post.right
                post.right.left = p

                p.left = post
                post.right = p

                # if self.pre_value_dic[val-1] == p:
                #     self.pre_value_dic[val-1] = p

                self.post_value_dic[val-1] = p  # 新的value字典
            else:
                if self.post_value_dic[val] !=p:
                    # if self.pre_value_dic[val] == p:
                    #     self.pre_value_dic[val] = p.right
                    post = self.post_value_dic[val]
                    self.updateValueDic(p,1)

                    p.left.right = p.right
                    p.right.left = p.left


                    p.right = post.right
                    post.right.left = p
                    post.right = p
                    p.left = post
                else:
                    self.updateValueDic(p,1)

                self.pre_value_dic[p.val] = p # 新的value字典
                self.post_value_dic[p.val] = p

        # tmp = self.head
        # while tmp:
        #     print(tmp.key, tmp.val, '----', tmp.left.key if tmp.left else 'None',
        #           tmp.right.key if tmp.right else 'None')
        #     tmp = tmp.right

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """

        if key in self.node_dic:
            self.updateNodeLeft(self.node_dic[key])

        else:
            p = DoubleNode(key,1)
            self.node_dic[key] = p
            self.insertNewNode(p)




    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """

        if key not in self.node_dic:
            return

        p = self.node_dic[key]

        self.updateNodeRight(p)



    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """

        # tmp = self.head
        # while tmp:
        #     print(tmp.key,tmp.val)
        #     tmp = tmp.right



        if self.head.right != self.tail:
            return self.head.right.key
        else:
            return ''


    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.tail.left != self.head:
            return self.tail.left.key
        else:
            return ''



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()