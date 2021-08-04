# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 14:31
# @Author  : zxl
# @FileName: 068_2.py

class Solution:
    def fullJustify(self, words , maxWidth: int) :


        i = 0

        lst = []

        while i<len(words):

            word_len = 0
            total_len = 0
            j = i

            while j<len(words) and total_len+len(words[j])<=maxWidth:

                word_len += len(words[j])
                total_len += (len(words[j])+1)

                j+=1

            s = ''
            if j-i ==1:
                s+=words[i]
                while len(s)<maxWidth:
                    s+=' '
            elif j>=len(words):
                for k in range(i,j-1):
                    s+=words[k]+' '
                s+=words[j-1]
                while len(s)<maxWidth:
                    s+=' '
            else:
                space_num = maxWidth-word_len
                a = space_num//(j-i-1)
                b = space_num-a*(j-i-1)

                for k in range(i,j-1):
                    s+=words[k]+' '*a
                    if b:
                        s+=' '
                        b-=1
                s+=words[j-1]
            lst.append(s)
            i = j
        return lst

