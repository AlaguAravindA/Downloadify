from flask import Flask, render_template, request
import videodown as vd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form['download_link']
        if link:
            try:                
                download = vd.download(link)
                
                return render_template('index.html', message="Download Successful!!!", download=download)
            except Exception as e:
                
                return render_template('index.html', error_message=e)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
