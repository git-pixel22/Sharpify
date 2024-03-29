from flask import Flask, render_template, request
import subprocess
import os
from queue import Queue

app = Flask(__name__)
requests = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global requests
    
    if request.method == "GET":
        return render_template("index.html")
    
    elif request.method == "POST":

        if 'imageInput' not in request.files:
            return 'No file part'

        file = request.files['imageInput']

        if file.filename == '':
            return 'No selected file'
        
        requests = requests + 1

        file.save(file.filename)

        # Deletes older output image
        output_file_path = os.path.join('static', 'output.png')
        if os.path.exists(output_file_path):
            os.remove(output_file_path)

        while True:    
            if requests == 1:
                command = f"backend/realesrgan-ncnn-vulkan -i {file.filename} -o static/output.png -n realesrgan-x4plus"
                subprocess.run(command, shell=True)
                requests = requests - 1
                break

        # DELETE INPUT
        os.remove(file.filename)

        # Pass the filename dynamically to the template
        output_image_path = "output.png"

        # Display the output image in output.html using Jinja syntax
        return render_template("output.html", output_image=output_image_path)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
