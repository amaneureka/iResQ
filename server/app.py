from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/hacker')
def hacker():
	return render_template('hacker.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)	