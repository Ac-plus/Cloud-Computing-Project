# import spacy
import re
import pandas as pd
import nltk 
from nltk.stem import WordNetLemmatizer
import langid
# nltk.download('wordnet')

def tokenize(text: str) :
    """
    对给定文本进行分词，返回token列表
    
    Args:
    text (str): 待处理的文本
    
    Returns:
    list: 文本分词后的token列表
    """
    
    # TODO: 实现tokenizedDocument函数.
    tokens = re.findall(r'\w+|[^\w\s]', text)
    # return ['It', 'has', '3', 'lines', ',', 'and', 'some', 'words', ',', 'like', 'https://www.baidu.com', 'and', '3020244000@tju.edu.cn', '.']
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

def tag_trans(tag:str) -> str:    # 词性转换，输出只能是n,v,s,a,r
    """
    "v" for verbs, 
    "a" for adjectives, 
    "r" for adverbs,
    "s" for satellite adjectives,
    "n" for nums.
    """
    if tag in ['VB', 'VBD', 'VBN', 'VBG', 'VBP', 'VBZ', 'MD']:
        return 'v'
    if tag in ['RB', 'RBR', 'RBS']:
        return 'r'
    if tag in ['SYN']:
        return 's'
    if tag in ['JJ', 'JJR', 'JJS']:
        return 'a'
    else:
        return 'n'

def getPos(w: str):
    wlist:list = []
    wlist.append(w)    
    pos_tag = nltk.pos_tag(wlist)
    pos = pos_tag[0][1]
    return pos

def getLemma(w: str):   # 获取单词的词根信息
    """
    对输入的单词w进行词形还原并返回其lemma
    """
    lemmatizer = WordNetLemmatizer()
    '''
    wlist = []
    wlist.append(w)    
    pos_tag = nltk.pos_tag(wlist)
    tag = pos_tag[0][1]
    '''
    tag = getPos(w)
    return lemmatizer.lemmatize(word=w, pos=tag_trans(tag))

def addLemmaDetails(documents: str) -> pd.DataFrame:
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
                'Type': tokenType(token),   #   'letters' if token.isalpha() else 'punctuation',
                'Language': langid.classify(token)[0],
                'PartOfSpeech': getPos(token),
                'Lemma': getLemma(token.lower())    # Only识别小写字母
            })
    
    # 将结果转换为DataFrame格式
    df = pd.DataFrame(tokens, columns=['Token', 'DocumentNumber', 'LineNumber', 'Type', 'Language', 'Lemma'])
    
    return df

# 测试
# 读取TXT文件并获得tokens详细信息
'''df = addLemmaDetails('./test.txt')

# 输出DataFrame
print(df.head(25))'''