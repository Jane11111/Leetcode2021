# -*- coding: utf-8 -*-
# @Time    : 2021-04-13 20:26
# @Author  : zxl
# @FileName: 20210403.py


class mystack():

    def __init__(self):

        self.lst = []

    def push(self,v):
        self.lst.append(v)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)


class myqueue():


    def __init__(self):

        self.lst1 = mystack()
        # self.lst2 = mystack()

    def push(self,v):


        tmp = mystack()
        while self.lst1.size() > 0:
            tmp.push(self.lst1.pop())
        self.lst1.push(v)
        while tmp.size()>0:
            self.lst1.push(tmp.pop())


    def pop(self):

        return self.lst1.pop()


class myqueue2():
    def __init__(self):
        self.lst1 = mystack()
        self.lst2 = mystack()

    def push(self,v):
        self.lst1.push(v)

    def pop(self):
        if self.lst2.size()>0:
            return self.lst2.pop()
        else:
            while self.lst1.size()>0:
                self.lst2.push(self.lst1.pop())
            return self.lst2.pop()




q = myqueue2()
q.push(1)
q.push(2)
q.push(3)
print(q.pop())
print(q.pop())
print(q.pop())


"""
双向链表，key value

# insert new_p:

p_tail.right = new_p
new_p.left = p_tail

# get v
从字典中找到v对应的指针 p

if p==p_head:
    p_head = p_head.right
    p_head.left = None
    p_tail.right = p
    p.left = p_tail
elif p== p_tail:
    pass
else:
    pre = p.left
    post = p.right
    





"""



