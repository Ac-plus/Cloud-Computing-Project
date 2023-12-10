#define your function here:
from bs4 import BeautifulSoup

def ismissing(tree):
    # 将tree转换为BeautifulSoup对象
    soup = BeautifulSoup(str(tree), 'html.parser')
    # 查找所有的元素
    elems = soup.find_all()

    # 创建一个和elems长度相同的逻辑数组
    tf = [1] * len(elems)

    # 检查每个元素是否引用了HTML树，若是则对对应的tf数组进行置0操作
    for i in range(len(elems)):
        if elems[i].parent is None:
            tf[i] = 0

    return tf