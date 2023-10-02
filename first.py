from flask import Flask
first = Flask(__name__)

@first.route('/')
def index():
    return render_html('index.html')

if __name__=="__main__":
    first.run()