from bs4 import BeautifulSoup

def extractHTMLText(html_text:str) -> str:
    
    soup = BeautifulSoup(html_text, 'html.parser')
    text = soup.get_text()
    return text