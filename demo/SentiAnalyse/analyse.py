from textblob import TextBlob
# from TDP.addPartOfSpeechDetails import addPartOfSpeechDetails

def SentiAnalyse(text:str)->int:
    blob = TextBlob(text)
    
    '''for i in range(len(blob.tags)):
        print("{}: {}".format(blob.tags[i][0], blob.tags[i][1]))'''

    sum = 0
    for i in range(len(blob.sentences)):
        # print("{}:情感倾向得分 {}".format(blob.sentences[i].string, blob.sentences[i].polarity))
        sum += blob.sentences[i].polarity
    sum /= len(blob.sentences)
    avg_point = sum *100
    return avg_point
