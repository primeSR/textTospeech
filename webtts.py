from flask import Flask, render_template
from flask import request, send_file
from flask.helpers import url_for
# from flask.helpers import url_for
from gtts import gTTS
import os
# from io import BytesIO
# import dropbox





app = Flask(__name__)

# port = int(os.getenv("PORT"))
port = int(os.environ.get("PORT",5000))
@app.route('/', methods = ['GET','POST'])
def web_tts():
  if request.method == "POST":
    lines = request.form.get('tts-text')
    # print(lines)
    text_to_speech = gTTS(lines)
    # print(gTTS(lines))

    i = 1
    path = './static/'
    # access_token = "c1uzg7s-JewAAAAAAAAAAcXaywdcn4aOKrW93zXVsz2G0xOvr9BSSeinUbqzZofg"
    # dbx = dropbox.Dropbox(access_token)
    if len(os.listdir(path)) == 0:
      text_to_speech.save('./static/speech.mp3')
      file = './static/speech.mp3'
      text = f"audio file speech.mp3 generated"
      # response = Response(open("./audio/speech.mp3", "rb"), content_type='audio/mp3')
    # tts_file = text_to_speech.write_to_fp(fp) # <-- gtts bytes file object 
    # dbx.files_upload(text_to_speech.save('./speech.mp3'),'/audio')
    else:
      for file in os.listdir(path):
                # print(file)
        if os.path.isfile('./static/speech.mp3'):
          text_to_speech.save(f'./static/speech{i}.mp3')
          file = f'./static/speech{i}.mp3'
          text = f"audio file speech{i}.mp3 generated"

          # if os.path.isfile(f'./static/speech{i}.mp3'):
          #   text = f"audio file speech{i}.mp3 generated"
          i += 1
    
    return render_template('index.html',text = text)

  return render_template('index.html')

@app.route('/')
def returnAudioFile():
    path_to_audio_file = "./static/"
    return send_file(
         path_to_audio_file, 
         mimetype="audio/mp3", 
         as_attachment=True)


if __name__ == '__main__':
  # app.run(debug=True)
  app.run(debug=True,host = '0.0.0.0',port = port)

