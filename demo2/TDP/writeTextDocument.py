def writeTextDocument(content: str, document: str):

    # 打开文件并写入内容
    with open(document, 'w', encoding='utf-8') as f:
        f.write(content)

