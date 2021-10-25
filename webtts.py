from flask import Flask, render_template
from flask import request, send_file
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
    text_to_speech = gTTS(lines)

    i = 1
    path = './audio/'
    # access_token = "c1uzg7s-JewAAAAAAAAAAcXaywdcn4aOKrW93zXVsz2G0xOvr9BSSeinUbqzZofg"
    # dbx = dropbox.Dropbox(access_token)
    if len(os.listdir(path)) == 0:
      text_to_speech.save('./audio/speech.mp3')
      # response = Response(open("./audio/speech.mp3", "rb"), content_type='audio/mp3')
    # tts_file = text_to_speech.write_to_fp(fp) # <-- gtts bytes file object 
    # dbx.files_upload(text_to_speech.save('./speech.mp3'),'/audio')
    else:
      for file in os.listdir(path):
                # print(file)
        if os.path.isfile('./audio/speech.mp3'):
          text_to_speech.save(f'./audio/speech{i}.mp3')
          # response = Response(open(f"./audio/speech{i}.mp3", "rb"), content_type='audio/mp3')
          # dbx.files_upload()

          i += 1

    # return render_template('index.html', file = "./audio/speech.mp3")
  return render_template('index.html')

@app.route('/<audio_file>')
def returnAudioFile(audio_file):
    path_to_audio_file = "./audio/" + audio_file
    response =  send_file(
         path_to_audio_file, 
         mimetype="audio/mp3", 
         as_attachment=True, 
          attachment_filename="speech.mp3")
    return render_template('index.html',file = response)


if __name__ == '__main__':
  app.run(debug=True,host = '0.0.0.0',port = port)

