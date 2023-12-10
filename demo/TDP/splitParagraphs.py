import re


def TokenizedDocument(document):
    """
    这是一个简单的token化函数，用于测试，功能是将一个文件标记为一个单词列表

    Args:
        document (str): 输入文件

    Returns:
        list: tokens列表
    """
    tokens = re.findall(r'\S+@\S+|\S+://\S+|\w+|\S+', document)
    return tokens


def splitParagraphs(input):
    # 判断输入类型
    if isinstance(input, str):
        # 按照双换行符或者单换行符进行分段
        paragraphs = re.split(r'\n\n|\r\n\r\n|\r\r|\n', input)
        # 去除首尾的空格
        paragraphs = [paragraph.strip() for paragraph in paragraphs]
        # 去除空段落
        paragraphs = [p for p in paragraphs if p]
        # 将分段后的文本以字符串数组形式返回
        return paragraphs
    elif isinstance(input, list) and all(isinstance(item, str) for item in input):
        # 对于已经token化的输入，先合并为一个字符串
        inputStr = ' '.join(input)
        # 调用上面的函数进行分段
        paragraphs = splitParagraphs(inputStr)
        # 将分段后的文本以字符串数组形式返回
        return paragraphs
    elif isinstance(input, list) and all(isinstance(item, TokenizedDocument) for item in input):
        # 对于已经token化的输入，先合并为一个TokenizedDocument
        combinedDoc = TokenizedDocument('')
        for doc in input:
            combinedDoc = combinedDoc + doc
        # 将TokenizedDocument按照分段符进行分段
        paragraphs = []
        currentParagraph = TokenizedDocument('')
        for token in combinedDoc:
            if token.text in ['\n\n', '\r\n\r\n', '\r\r', '\n']:
                if len(currentParagraph) > 0:
                    paragraphs.append(currentParagraph)
                    currentParagraph = TokenizedDocument('')
            else:
                currentParagraph.append(token)
        if len(currentParagraph) > 0:
            paragraphs.append(currentParagraph)
        # 将分段后的文本以TokenizedDocument数组形式返回
        return paragraphs
    else:
        # 如果输入类型不正确，抛出异常
        raise TypeError('Input should be either a string or a list of strings (tokenized documents)')

# # 示例用法
# with open("test.txt", "r", encoding="utf-8") as f:
#     text = f.read()

# if type(text) == str:
#     paragraphs = splitParagraphs(text)
#     print(paragraphs)
# else:
#     raise TypeError('Input should be a string.')
