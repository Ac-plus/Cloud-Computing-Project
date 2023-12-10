# 功能: 将HTML和XML实体转换为字符串

import html.parser
import html

def decodeHTMLEntities(text: str):
    """
    Convert HTML and XML entities into characters
    
    Args:
        text (str): 待转换的文本
    
    Returns:
        str: 转换后的文本
    """
    
    parser = html.parser.HTMLParser()
    new_text = html.unescape(text)
    return new_text

# 测试
'''
print(decodeHTMLEntities("R&amp;D"))    # 输出 R&D
print(decodeHTMLEntities("&lt;&gt;"))   # 输出 <>
print(decodeHTMLEntities("R&#x20;D"))   # 输出 R D
'''
