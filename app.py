from flask import Flask, render_template, request
import subprocess
import os

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

        # DELETE THIS FILE AFTER USE
        file.save(file.filename)

        #if ouptut.png image exists under static folder, delete it.
        output_file_path = os.path.join('static', 'output.png')
        if os.path.exists(output_file_path):
            os.remove(output_file_path)

        # run the executable (currently the output file is saved inside backend folder)
        command = f"backend/realesrgan-ncnn-vulkan -i {file.filename} -o static/output.png -n realesrgan-x4plus"
        subprocess.run(command, shell=True)

        #DELETE INPUT
        os.remove(file.filename)

        # Pass the filename dynamically to the template
        output_image_path = "output.png"

        # dislay the output image in output.html using jinja syntax
        return render_template("output.html", output_image=output_image_path)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
