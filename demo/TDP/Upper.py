# 功能: 将text文件、string字符串中的全部大写字母变为小写
# 说明: 支持英语之外的非ASCII字符，如德语等

import os

def Upper(documents: str, new_documents: str = None, mode: str = "String") :
    # 参数说明：
    # documents:        文件名或字符串内容
    # new_documents:    需要写入的新文件名，默认为空
    # mode:             需要转换的数据格式，目前支持字符串"String"和文本文件"Text"

    if mode=="String" : # 表示需要转换字符串
        return documents.upper()
    if mode=="Text" :   # 表示需要读取txt文档
        if not(documents.endswith(".txt") == 1):
            raise Exception(f"Document '{documents}' is not a text file.")

        #   文件读取，变更大小写后重新保存一个文件
        #   读取文件，重命名为f
        l=[]
        with open(documents,'r',encoding='utf-8') as f:
            for i in f:
                for i2 in i:
                    l.append(i2.upper())
        l3=''.join(l)
        # print(l3)

        #   转成小写，准备写入文件里
        f = open(new_documents, 'w', encoding='utf-8')
        print(l3, file=f, end='')
        '''
        with open(new_documents,'w',encoding='utf-8') as f:
            with open(new_documents,'w',encoding='utf-8') as f1:
                for i in f.readlines():
                    f1.write(i.lower())
        f1.close()
        '''

    else :
        raise Exception(f"Function lower() needs correct mode: String or Text.")

#   测试样例1：字符串
'''print(Upper("ASDFGHBfdtrthgJhgsftERTY"))

#   测试样例2：文本文件
documents =     "test.txt"
new_documents = "test_lower.txt"
Upper(documents, new_documents, mode="Text")
with open(new_documents, "r") as f:    #   打开文件
    data = f.read()   # 读取文件
    print(data)'''

 
        