# import os
# from dotenv import load_dotenv
# from openai import OpenAI
# from flask import Flask, render_template

# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_APIKEY"))

# # Flask app
# app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/behavioral-question", methods=["POST"])
# def behavioral_question():
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a recruiter for Data Scientists at one of the leading tech firms.",
#             },
#             {
#                 "role": "user",
#                 "content": "Generate a typical behavioral interview question. Only show the question in your response.",
#             },
#         ],
#         max_tokens=100,
#     )
#     return response.choices[0].message.content


# @app.route("/technical-question", methods=["POST"])
# def technical_question():
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a recruiter for Data Scientists at one of the leading tech firms.",
#             },
#             {
#                 "role": "user",
#                 "content": "Generate a typical technical interview question. Only show the question in your response.",
#             },
#         ],
#         max_tokens=100,
#     )
#     return response.choices[0].message.content


# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=5000)
import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)