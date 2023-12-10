import re
import pandas as pd
import nltk 
from nltk.stem import WordNetLemmatizer
import langid

def tokenize(text: str) :
    """
    对给定文本进行分词，返回token列表
    
    Args:
    text (str): 待处理的文本
    
    Returns:
    list: 文本分词后的token列表
    """
    
    # TODO: 实现tokenizedDocument函数.
    tokens = re.findall(r'\S+@\S+|\S+://\S+|\w+|\S+', text)
    # return ['It', 'has', '3', 'lines', ',', 'and', 'some', 'words', ',', 'like', 'https://www.baidu.com', 'and', '3020244000@tju.edu.cn', '.']
    # print(tokens)
    return tokens

def tokenType(token: str) -> str: # 判断token类别
    """
    根据输入的token，返回对应的类别
    
    Args:
    token (str): 待处理的token
    
    Returns:
    str: token的类别
    """
    if re.match(r'^[a-zA-Z]+$', token):
        # 数字
        return 'letters'
    if re.match(r'^[0-9]+$', token):
        # 普通的英文单词
        return 'numbers'
    elif re.match(r'^(:\)|:D|:\(|qwq|qaq)$', token):
        # emoji表情
        return 'emotion'
    elif re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', token):
        # email地址
        return 'email'
    elif re.match(r'^(http|https)://.+', token):
        # URL地址
        return 'URL'
    elif re.match(u'[\u0020-\u007F\u2000-\u206F\u3000-\u303F\uff01-\uffee]', token):
        # 标点符号
        return 'punctuation'
    else:
        return 'others'

def getPos(w: str) -> str:
    """
    获取单词w的词性
    Inputs
        w:str   英文单词
    Returns
        pos:str 词性
    """
    wlist:list = []
    wlist.append(w)    
    pos_tag = nltk.pos_tag(wlist)
    pos = pos_tag[0][1]
    return pos

def addPartOfSpeechDetails(documents: str) -> pd.DataFrame:
    """
    返回一个包含tokens详细信息的表格，增加了每个单词的词元
    
    Args:
    documents (str): 一个待处理的文本文件名
    
    Returns:
    pandas.DataFrame: 包含tokens详细信息的DataFrame
    """
    
    # 读取文件内容
    with open(documents, 'rt', encoding='utf-8') as f:
        text = f.read()
    
    # 对文本进行分词
    tokens = []
    lines = text.split('\n')
    for i, line in enumerate(lines):
        doc_tokens = tokenize(line)
        for j, token in enumerate(doc_tokens):
            tokens.append({
                'Token': token,
                'DocumentNumber': i + 1,
                'LineNumber': j + 1,
                'SentNumber': 1,
                'Type': tokenType(token),   #   'letters' if token.isalpha() else 'punctuation',
                'Language': langid.classify(token)[0],
                'PartOfSpeech': getPos(token)
            })
        # end for
    # end for
    
    # 将结果转换为DataFrame格式
    df = pd.DataFrame(tokens, columns=['Token', 'DocumentNumber', 'LineNumber', 'SentNumber', 'Type', 'Language', 'PartOfSpeech'])
    
    # 修改SentenceNumner
    last_row = None
    for index, row in df.iterrows():
        if index == 0:
            row['SentNumber'] = 1
        else:
            if df.at[index-1, 'Token'] in ['!','?','.'] :
                # row['SentNumber'] = last_row['SentNumber'] + 1
                df.at[index, 'SentNumber'] = df.at[index-1, 'SentNumber'] + 1
                # print(row['SentNumber'])
            else :
                # row['SentNumber'] = last_row['SentNumber']
                df.at[index, 'SentNumber'] = df.at[index-1, 'SentNumber']
        last_row = row
                
    return df

# 测试
# 读取txt文件并获得tokens详细信息
'''df = addPartOfSpeechDetails('./test.txt')

# 输出DataFrame
print(df.head(25))'''