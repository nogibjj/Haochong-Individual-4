import os
from dotenv import load_dotenv
import time
from openai import OpenAI
from flask import Flask, render_template, request

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_APIKEY"))

# Define a simple rate limiter
last_request_time = 0
MIN_TIME_BETWEEN_REQUESTS = 2  # Set the minimum time between requests in seconds


app = Flask(__name__)


def generate_prompt(category):
    if category == "physical":
        return "Generate a physical health suggestion."
    elif category == "mental":
        return "Generate a mental health suggestion."


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    global last_request_time

    # Check if enough time has passed since the last request
    current_time = time.time()
    if current_time - last_request_time < MIN_TIME_BETWEEN_REQUESTS:
        return "Too many requests. Please try again later."

    category = request.form["category"]
    prompt = generate_prompt(category)

    # Use the new OpenAI interface
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a consultant providing health suggestions.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        max_tokens=150,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    app.run(debug=True)
