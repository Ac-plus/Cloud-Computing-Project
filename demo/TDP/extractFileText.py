#define your function here:

def extractFileText(file_path: str, Pages: list = None, Password : str=None) -> str:
    # get suffix
    # support txt pdf doc/docx html
    # extractFileText as str
    suffix = file_path.split('.')[-1]

    content = ''
    if suffix == 'txt':
        with open(file_path, 'r') as f:
            content = f.read()
        f.close()

    elif suffix == 'pdf':
        import pdfplumber
        with pdfplumber.open(file_path , password = Password) as pdf:
            # return Pages is None
            if Pages is None:
                pages_to_extract = range(len(pdf.pages))
            else:
                pages_to_extract = Pages
            for id in pages_to_extract:
                text = pdf.pages[id].extract_text()
                content += text
            return content
    elif suffix == 'docx' or suffix == 'doc':
        import docx
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            content += para.text
    elif suffix == 'html':
        from bs4 import BeautifulSoup
        with open(file_path, 'r') as f:
            html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            content = soup.get_text()
            f.close()

    return content