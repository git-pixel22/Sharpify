from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")
    
    elif request.method == "POST":

        if 'imageInput' not in request.files:
            return 'No file part'

        file = request.files['imageInput']

        if file.filename == '':
            return 'No selected file'

        file.save(file.filename)

        # run the executable

        # save the output image in /static

        # dislay the output image in output.html using jinja syntax

        # # Generating audio file paths with dynamic names
        # audio_files = [
        #     f"./static/output_{name.lower()}.wav" for name in audio_names
        # ]

        # # Enumerating the audio files and names as a list of tuples
        # enumerated_audio = list(zip(audio_names, audio_files))

        # return render_template("output.html", enumerated_audio=enumerated_audio)

    return render_template("output.html")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
