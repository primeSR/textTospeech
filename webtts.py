from flask import Flask, render_template
from flask import request, send_file

from gtts import gTTS
import os

import gtts

# from werkzeug.wrappers import response




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
    path = 'static/'
    if len(os.listdir(path)) == 0:
      text_to_speech.save('static/speech.mp3')
      file = 'static/speech.mp3'
      text = f"audio file speech.mp3 generated"
    else:
      for file in os.listdir(path):
        if os.path.isfile('static/speech.mp3'):
          text_to_speech.save(f'static/speech{i}.mp3')
          file = f'static/speech{i}.mp3'
          text = f"audio file speech{i}.mp3 generated"

          i += 1
    
    return render_template('index.html',text = text, file = file)

  if request.method == "GET":
    lines = request.args.get('text')
    if lines is None:
      pass
    else:
      tts = gTTS(lines)
      i = 1
      path = 'static/'
      if len(os.listdir(path)) == 0:
        tts.save('static/speech.mp3')
        file_url = 'static/speech.mp3'
        # text = f"audio file speech.mp3 generated"
      else:
        for file in os.listdir(path):
          if os.path.isfile('static/speech.mp3'):
            tts.save(f'static/speech{i}.mp3')
            file_url = f'static/speech{i}.mp3'
            # text = f"audio file speech{i}.mp3 generated"

            i += 1

      return request.base_url+file_url

  return render_template('index.html')




@app.route('/static/<audio_file_name>', methods = ['GET'])
def returnAudioFile(audio_file_name):
  path_to_audio_file = "./static/" + audio_file_name
  return send_file(path_to_audio_file,mimetype="audio/mp3",as_attachment=True,download_name=audio_file_name)
  


  


if __name__ == '__main__':
  # app.run(debug=True)
  app.run(debug=True,host = '0.0.0.0',port = port)

