from flask import Flask
from Utils import SCORES_FILE_NAME

app = Flask(__name__)

@app.route('/')
def main_page():
    return "<html><head><title>World of games</title></head><body><h1>Welcome to the world of games</h1><hr/>" \
           "<p><a href='scores'>View score</a></p></body>";

@app.route('/scores')
def score_server():
    try:
        score_text = ''
        style_text = ''
        with open(SCORES_FILE_NAME, 'r') as file:
            score_text = file.read()
    except BaseException as e:
        style_text = 'style="color:red"'
    return f'<html><head><title>Scores Game</title></head><body>' \
           f'<h1>The score is <div id="score" {style_text}>{score_text}</div></h1>' \
           f'</body></html>'

