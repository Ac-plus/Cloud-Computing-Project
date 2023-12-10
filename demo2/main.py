from asyncio import sleep
import bs4
from bs4 import BeautifulSoup
import requests
from TDP.decodeHTMLEntities import decodeHTMLEntities
from TDP.eraseTags import eraseTags
from TDP.extractHTMLText import extractHTMLText
from TDP.getAttribute import getAttribute
from TDP.ismissing import ismissing
from TDP.string import string
from TDP.writeTextDocument import writeTextDocument

def get_html(url):
    res = requests.get(url)
    html = res.content.decode('utf-8')
    return html

def clean_html(html_code):
    # 使用 BeautifulSoup 解析 HTML 代码
    soup = BeautifulSoup(html_code, 'html.parser')
    
    # 删除空元素
    is_missing = ismissing(soup)
    if True in is_missing and len(is_missing)==len(soup.contents):
        for i in range(len(is_missing)):
            # 检查节点是否为文档类型节点
            '''if isinstance(soup.contents[i], str) and soup.contents[i].strip() == '':
                continue'''
            
            if is_missing[i] and type(soup.contents[i])==bs4.element.Tag:
                soup.contents[i].decompose()
                # print(type(doc))
    else:
        print(len(is_missing))
        print(len(soup.contents))
        # sleep(1)

    # 获取所有链接的 href 属性值
    links = getAttribute(soup.find_all('a'), 'href')
    # print('Links:', links)

    # 清理标记符号和空格
    clean_text = eraseTags(str(soup))
    # clean_text = spaces(clean_text)

    # 将解析的 HTML 树转换为字符串
    html_str = string(soup)

    # 解码 HTML 实体字符
    decoded_html = decodeHTMLEntities(html_str)

    # 提取 HTML 代码中的纯文本内容
    text = extractHTMLText(html_code)

    return text

# 测试样例
url = 'https://www.sina.com.cn/'
obj_file = "./demo2/sina.txt"

html_code = get_html(url)
# print(html_code)
text = clean_html(html_code)
writeTextDocument(text, obj_file)

# 清除空行
with open(obj_file, 'r',encoding='utf-8') as f:
    # 读取文件中的所有内容
    text = f.read()

lines = text.split('\n')
new_text = '\n'.join(line for line in lines if line.strip())

with open(obj_file, 'w',encoding='utf-8') as f:
    f.write(new_text)
