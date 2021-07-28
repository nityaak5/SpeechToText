from flask import Flask, render_template, request, redirect
import speech_recognition as sr


app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    transcript= ""
    if request.method== 'POST':
        print("data received")

        if "file" not in request.files:
            print("blank duh")
            redirect(request.url)
        
        file=request.files['file']
        if file.filename=='':
            print("blank duh")
            return redirect(request.url)
        
        if file:

            recognizer=sr.Recognizer()                          #creating a recognizer class
            audioFile= sr.AudioFile(file)                       #audiofile object

            with audioFile as source:                           #opening the audio file
                audio=recognizer.record(source)                 #reading audio file using recognizer              #
                print("audio recieved")
                
                transcript=recognizer.recognize_google(audio, key=None)      #recognizing the audio using google api
                
            
    return render_template('index.html', transcript=transcript)


if __name__ == '__main__':
    app.run(debug= True, threaded= True)
 