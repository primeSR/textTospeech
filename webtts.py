from flask import Flask, render_template
from flask import request
from gtts import gTTS
import os

from io import BytesIO
import audioplayer

app = Flask(__name__)


# port = int(os.environ.get("PORT",5000))
@app.route('/', methods = ['GET','POST'])
def web_tts():
  if request.method == "POST":
    lines = request.form.get('tts-text')
    fp = BytesIO()
    # print(lines)
    # file = './static/tts.mp3'
    text_to_speech = gTTS(lines)
    # text_to_speech.write_to_fp(fp)
    text_to_speech.save('./tts.mp3')
    audioplayer.AudioPlayer('./tts.mp3').play(block=True)
    os.remove('./tts.mp3')


  return render_template('index.html')

# @app.route('/')
# def returnAudioFile():
#     path_to_audio_file = "./static/"
#     return send_file(
#          path_to_audio_file, 
#          mimetype="audio/mp3", 
#          as_attachment=True)


if __name__ == '__main__':
  app.run(debug=True)
  # app.run(debug=True,host = '0.0.0.0',port = port)

