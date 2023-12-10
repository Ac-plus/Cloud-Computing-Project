#define your function here:
from bs4 import BeautifulSoup

def string(tree):
    soup = BeautifulSoup(str(tree), 'html.parser')
    strText = soup.prettify()
    return strText