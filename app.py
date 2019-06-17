import json

from flask import Flask, request

from acronamer import *



app = Flask(__name__)

@app.route('/')
def endpoints():
    return('try /get-acronyms')


@app.route('/get-acronyms')
def return_acronyms_via_api():
    try:
        words = request.args.get('words').split(',')
        data = acronamer(words)
        return json.dumps({'data':data})
    except Exception as e:
        return json.dumps({'error':str(e)})
        


if __name__ == '__main__':
    app.run(debug=True)



