#define your function here:
from bs4 import BeautifulSoup

def eraseTags(text):
    # 创建BeautifulSoup对象
    soup = BeautifulSoup(text, 'html.parser')
    # 获取所有文本内容
    result = soup.get_text(separator=' ')
    return result
