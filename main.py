import openai
from flask import Flask, render_template, request
import tensorflow as tf
openai.api_key = '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'
#load trained NLP model using TensorFlow here

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.form['topic']

#Generate content with trained NLP model here

generated_content = "This is a generated article about " + topic 
return render_template('index.html', generated_content=generated_content)

if  __name__ == '__main__':
    app.run(debug=True)