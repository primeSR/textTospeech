from gtts import gTTS
import os
# import librosa


with open('textFile.txt','r',encoding='utf-8') as text_file:
    lines = text_file.read()
    # lines = text_file.readlines()
    # print(type(lines))
    text_to_speech = gTTS(lines)
    i = 1
    path = './audio/'
    try:
        if len(os.listdir(path)) == 0:
            text_to_speech.save('./audio/speech.mp3')
        else:
            for file in os.listdir(path):
                # print(file)
                if os.path.isfile(f'./audio/{file}'):
                    text_to_speech.save(f'./audio/speech{i}.mp3')
                    i+=1
    except Exception as e:
        print(e)
            


