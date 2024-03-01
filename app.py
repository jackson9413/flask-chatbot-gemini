from flask import Flask, request, render_template
import os
import dotenv
import google.generativeai as genai
import markdown

dotenv.load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['GET', 'POST'])
def chat():
    msg = request.form['msg']
    input_text = msg 
    response = model.generate_content(input_text)
    return response.text


if __name__ == '__main__':
    app.run(debug=True)