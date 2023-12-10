from logging import raiseExceptions
import pandas as pd
from typing import List
import re

def removePunctuation(text):
    # python 去除字符串的标点符号
    punctuation = '!,;:?"\'、，；'
    text = re.sub(r'[{}]+'.format(punctuation),' ',text)
    return text.strip()

def ngram_eq(tokens: list, ngram: list, n: int, index: int):
    # list里的第index个token开始的长度为n的子序列是否和ngram相等
    for i in range(index, index+n):
        if removePunctuation(tokens[i]) != ngram[i-index]:
            return False
    return True

def Context(documents: str, text: str, ngram: list[str] = None) -> pd.DataFrame:
    """
    返回一个包含文本text所在位置详细信息的表格   

    Args:
        documents (str):    一个待处理的文本文件名
        text:               待搜索的文本内容 

    Returns:
        pandas.DataFrame:   包含text所在位置详细信息的DataFrame

    """

    # 读取文件内容
    with open(documents, 'rt', encoding='utf-8') as f:
        lines = f.read()

    # 将文本分割成多行并存储在列表中
    lines = lines.split('\n')
    
    if text != None and ngram == None:  # 需要搜索的是word

        # 逐行搜索含有指定字符串的文本，并将结果存储在列表中
        results = []
        # print((lines))
        for i, line in enumerate(lines):
            # print(line)
            if text in line:
                # print("text in line")
                # 将文本分割成单词或n-gram，并存储在列表中
                tokens = line.split()
                # print(tokens)
                for j, token in enumerate(tokens):
                    if text == removePunctuation(token) :   ### NOTICE 原来是in，那样就会搜索出全部字串了，改为==可能可以唯一匹配单词 updatelog: 改为text去除标点
                        # 获取当前单词或n-gram周围的若干个单词
                        start = max(0, j - 9)
                        end = min(len(tokens), j + 9)
                        data_context = ' '.join(tokens[start:end])
                        
                        # 将结果添加到列表里
                        results.append({
                            'Context': data_context,
                            'Document': i + 1,
                            'Index': j + 1
                        
                        })
                        
        # 将结果转换为pandas数据框并返回
        return pd.DataFrame(results)

    if text == None and ngram != None:      # 需要搜索的是ngram，即连续的多个单词
        n = len(ngram)                      # n-gram的规模
        results = []
        for i, line in enumerate(lines):    # 逐行搜索含有指定字符串的文本，并将结果存储在列表中
            ngram_str = ' '.join(ngram[0:n-1])
            if ngram_str in line:
                tokens = line.split()       # 将文本分割成单词或n-gram，并存储在列表中
                # print(tokens)
                for j, token in enumerate(tokens):
                    if ngram_eq(tokens, ngram, n, j):       
                        
                        # 获取当前单词或n-gram周围的若干个单词
                        start = max(0, j - 4)
                        end = min(len(tokens), j + 5)
                        data_context = ' '.join(tokens[start:end])
                        
                        # 将结果添加到列表里
                        results.append({
                            'Context': data_context,
                            'Document': i + 1,
                            'Index': j + 1
                        
                        })
                        
        # 将结果转换为pandas数据框并返回
        return pd.DataFrame(results)


    
    if text != None and ngram != None:
        raiseExceptions("You can't assign both word and ngram !")
    
    if text == None and ngram == None:
        raiseExceptions("You can't assign both word and ngram as None !")
        



'''documents = './test.txt'
text = 'Tianjin'
ngram = ['Tianjin','University']
result = Context(documents, text=None,ngram=ngram)
print(result)'''

