import re

def tokenizedDocument(text: str) :
    """
    对给定文本进行分词，返回token列表
    
    Args:
    text (str): 待处理的文本
    
    Returns:
    list: 文本分词后的token列表
    """

    tokens = re.findall(r'\S+@\S+|\S+://\S+|\w+|\S+', text)
    # print(tokens)
    return tokens