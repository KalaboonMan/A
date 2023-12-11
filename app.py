from flask import Flask , render_template, request, redirect , url_for

app = Flask(__name__)

courses = [
    {'code' : 'TH001', 'name': 'Thai'},
    {'code' : 'Eng002', 'name': 'English'},
    {'code' : 'IR003', 'name': 'IR'},
]

@app.route('/')
def index():
    return render_template('index.html', courses = courses)

if __name__ == '__main__':
    app.run(debug=True)