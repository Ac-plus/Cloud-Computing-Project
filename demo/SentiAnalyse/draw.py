import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_wordcloud(word_list):
    """
    基于给定的单词列表生成词云图
    
    Args:
    word_list (list): 待处理的单词列表
    
    Returns:
    None
    """
    
    # 将单词列表转换为字符串
    text = ' '.join(word_list)
    
    # 创建WordCloud对象
    wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(text)
    
    # 绘制词云图
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    
    # 显示图像
    plt.show()

# generate_wordcloud(['list', "word"])