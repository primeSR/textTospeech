from flask import Flask, render_template
from flask import request, send_file

from gtts import gTTS
import os
import datetime




app = Flask(__name__)

port = int(os.environ.get("PORT",5000))
@app.route('/', methods = ['GET','POST'])
def web_tts():
  if request.method == "POST":
    lines = request.form.get('tts-text')
    text_to_speech = gTTS(lines)

    base_name = 'aud'
    suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    file_name = "_".join([base_name,suffix])

    text_to_speech.save(f'static/{file_name}.mp3')
    audio_file = f'static/{file_name}.mp3'
    text = f"audio file {file_name}.mp3 generated"



    return render_template('index.html',text = text, file = audio_file)

  if request.method == "GET":
    lines = request.args.get('text')
    if lines is None:
      pass
    else:
      tts = gTTS(lines)
      base_name = 'aud'
      suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
      file_name = "_".join([base_name, suffix])

      tts.save(f'static/{file_name}.mp3')
      file_url = f'static/{file_name}.mp3'
 
      return request.base_url+file_url

  return render_template('index.html')

@app.route('/file_val',methods = ['POST'])
def remove_file_after_play():
  file_val = request.get_data()
  
  print({"file_value":file_val})
  try:
    os.remove(file_val)
    print("file removed")
  except Exception as e:
    print(e)

  return render_template('index.html')
  




@app.route('/static/<audio_file_name>', methods = ['GET'])
def returnAudioFile(audio_file_name):
  path_to_audio_file = "./static/" + audio_file_name
  
  # acc_time = os.stat(path_to_audio_file).st_atime
  
  # print(acc_time)
  return send_file(path_to_audio_file,mimetype="audio/mp3",as_attachment=True,download_name=audio_file_name)
  


  


if __name__ == '__main__':
  # app.run(debug=True)
  app.run(debug=True,host = '0.0.0.0',port = port)

