import os

from flask import *

app = Flask(__name__)
UPLOAD_FOLDER = 'selfies/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def upload():
    return render_template("file_upload_form.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return render_template("success.html", name=f.filename)


if __name__ == '__main__':
    app.run(debug=True)

    """        <input type="file"  name="file" alt="Submit" accept="image/*" capture="camera"/>
        <input type = "submit" value="Upload">     """
