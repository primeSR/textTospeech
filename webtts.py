from flask import Flask, render_template
from flask import request
# from flask.helpers import url_for
from gtts import gTTS
# import os
# from io import BytesIO
# import dropbox
# from flask_wtf.csrf import CSRFProtect





app = Flask(__name__)
# csrf = CSRFProtect(app)

@app.route('/demo/', methods = ['GET','POST'])
def web_tts():
  if request.method == "POST":
    lines = request.form.get('tts-text')
    # lines = written.read()
    text_to_speech = gTTS(lines)
    # fp = BytesIO()
    # print(fp)
    # i = 1
    # path = './audio/'
    access_token = "c1uzg7s-JewAAAAAAAAAAcXaywdcn4aOKrW93zXVsz2G0xOvr9BSSeinUbqzZofg"
    dbx = dropbox.Dropbox(access_token)
    # dbx.check_and_refresh_access_token()
    # print(dbx.check_and_refresh_access_token())

    # try:
    # if len(os.listdir(path)) == 0:
    text_to_speech.save('./speech.mp3')
    # tts_file = text_to_speech.write_to_fp(fp) # <-- gtts bytes file object
    # tts_file = text_to_speech.save('./speech.mp3')
    # print(tts_file)
    # dbx.files_upload(tts_file,'/speech.mp3')
    #     else:
          
    #       for file in os.listdir(path):
    #             # print(file)
    #           if os.path.isfile(f'./audio/{file}'):
    #             text_to_speech.save(f'./audio/speech{i}.mp3')
    #             dbx.files_upload()

    #             i += 1
                  
    # except Exception as e:
    #     print(e)
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)

