# -*- coding: utf-8 -*-
# @Time    : 2021-06-29 11:06
# @Author  : zxl
# @FileName: 068.py


class Solution:
    def fullJustify(self, words , maxWidth: int) :

        ans = []

        i = 0
        while i<len(words):

            l = len(words[i])
            wordlen = l
            wordcount = 1

            j = i
            while j+1<len(words) and l+1+len(words[j+1])<=maxWidth:
                j+=1
                wordlen+=len(words[j])
                l+=len(words[j])+1
                wordcount+=1

            space_num = maxWidth-wordlen

            new_s = words[i]
            if wordcount != 1:
                if j+1 == len(words):
                    a = 1
                    b = 0
                else:
                    a = space_num//(wordcount-1)
                    b = space_num%(wordcount-1)
                i+=1
                while i!=j+1:
                    spaces = ' '*((a+1) if b else (a))

                    new_s += spaces
                    new_s += words[i]
                    i+=1
                    if b:
                        b -= 1
            while len(new_s) != maxWidth:
                new_s += ' '
            ans.append(new_s)

            i = j+1
        return ans

obj = Solution()
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]


maxWidth = 20
ans = obj.fullJustify(words,maxWidth)
print(ans)