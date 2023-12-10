#define your function here:
import string
import re

def erasePunctuation(text):
    # python 去除字符串的标点符号
    punctuation = '!,;:?"\'、，；'
    text = re.sub(r'[{}]+'.format(punctuation),' ',text)
    return text.strip()

# print(erasePunctuation("Hello, world"))