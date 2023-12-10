from TDP.addLemmaDetails import addLemmaDetails
from TDP.extractFileText import extractFileText
from TDP.splitParagraphs import splitParagraphs
from TDP.addPartOfSpeechDetails import addPartOfSpeechDetails
from TDP.addSentenceDetail import addSentenceDetails
from TDP.context import Context
from TDP.Lower import Lower
from TDP.tokenDetails import TokenDetails
from TDP.Upper import Upper
from TDP.tokenizedDocument import tokenizedDocument
from SentiAnalyse.analyse import SentiAnalyse
from TDP.removeStopWords import removeStopWords
from TDP.erasePunctuation import erasePunctuation
from SentiAnalyse.draw import generate_wordcloud
from decimal import Decimal

welcoming_msg = '''#-------------------------------------------#
|     Chatting File Management System       | 
|     Welcome you!                          |
|     You can input some words              |
|     Then we will search for you.          |
#-------------------------------------------# 
'''
print(Upper(welcoming_msg))

chatting_file = "./demo/chatting.txt"
# 首先，分析单词数目
'''with open(chatting_file, 'rt', encoding='utf-8') as f:
    text = f.read()'''
text = extractFileText(chatting_file)

tokens = []
# lines = text.split('\n')
lines = splitParagraphs(text)
td = TokenDetails(lines)
token_count = td.shape[0]
word_count = (td['Type'] == 'letters').sum()
print("[INFO] The chatting have", token_count, "tokens, including", word_count, "words.")

# 接下来，绘制词云图
# 首先，提取全部单词的原型
print("[INFO] Generating WordCloud for you ...")
lemmas = addLemmaDetails(chatting_file)["Lemma"].to_list()
generate_wordcloud(lemmas)

# 搜索单词
print("[INFO] Please Input text: ")
search_text = input()
print("[INFO] We are searching for {} in chatting file ...".format(search_text))
if len(Lower(search_text)) > 1:
    result = Context(
        chatting_file, 
        text = None,
        ngram = tokenizedDocument(search_text)
    )
elif len(Lower(search_text)) == 1:
    result = Context(
        chatting_file, 
        text = tokenizedDocument(search_text)[0]
    )
else:
    raise Exception("Input Text Error!")

print("[INFO] Successfully searched for you, positions of text {} are as follows:".format(search_text))
docNum = result["Document"].to_list() # 提取出要从lines查找第几行

points = [] # 情感得分数组
for i in docNum:    # 遍历lines文本
    point = (
        SentiAnalyse(
            removeStopWords(
                erasePunctuation(lines[i])
                )
            )
        ) # 将对应的Context作情感分析
    points.append(Decimal(point).quantize(Decimal("0.00")))
result["SentiPoint"] = points

print(result)
