# import spacy
import re
import pandas as pd

import re

def get_token_language(token: str) -> str:
    """
    判断 token 所属的语言

    参数：
    - token: 待判断的字符串，字符串类型

    返回值：
    - 字符串类型的语言标识，例如 'en' 表示英文，'zh' 表示中文，'ja' 表示日语等。
    """
    # 匹配英文单词、数字或者只有标点符号的单个字符
    if re.match(r'^[\w!@#$%^&*(),.?":{}|<>\[\]\-\\\/]+$', token):
        return 'en'

    # 匹配汉字
    elif re.match(r'^[\u4e00-\u9fa5]+$', token):
        return 'zh'

    # 匹配韩文音节和汉字
    elif re.match(r'^[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f\u3200-\u32ff\ua960-\ua97f]+$',
                token):
        return 'ko'

    # 匹配其他语言
    else:
        return 'other'

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

def TokenDetails(documents: list) -> pd.DataFrame:
    """
    返回一个包含tokens详细信息的表格
    
    Args:
    documents (str): 一个待处理的文本字符串数组。
        Eg.["Hello", "Worlds", "!"]
           [["Hello", "Worlds", "!"], ["Hello", "TJU", ":D"]]
    
    Returns:
    pandas.DataFrame: 包含tokens详细信息的DataFrame
    """
    
    # 读取文件内容
    '''with open(documents, 'rt', encoding='utf-8') as f:
        text = f.read()
    '''
    # 对文本进行分词
    tokens = []
    # lines = text.split('\n')
    lines = documents
    for i, line in enumerate(lines):
        # doc_tokens = tokenize(line)
        doc_tokens = lines[i]
        for j, token in enumerate(doc_tokens):
            tokens.append({
                'Token': token,
                'DocumentNumber': i + 1,
                'LineNumber': j + 1,
                'Type': tokenType(token),   #   'letters' if token.isalpha() else 'punctuation',
                'Language': get_token_language(token),
            })
    
    # 将结果转换为DataFrame格式
    df = pd.DataFrame(tokens, columns=['Token', 'DocumentNumber', 'LineNumber', 'Type', 'Language'])
    
    return df

# 测试
# 读取TXT文件并获得tokens详细信息
'''text1 = [
    ["Hello", "Worlds", "!"], 
    ["Hello", "TJU", ":D"]
]
text2 = [
    ["Michael", "has", "1", "new", "email", ":", "michael@tju.edu.cn", "."], 
    ["Hello", "TJU", ":)"],
    ["Michael", "is", "proud", "of", "his", "website", ":", "https://www.michael.com", "."]
]
df = tokenDetails(text2)

# 输出DataFrame
print(df)'''