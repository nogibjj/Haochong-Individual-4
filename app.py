import os
from dotenv import load_dotenv
import time
import openai
import random
from flask import Flask, render_template, request, jsonify

load_dotenv()
openai.api_key = os.getenv("OPENAI_APIKEY")


# Define a simple rate limiter
last_request_time = 0

app = Flask(__name__)


def generate_prompt(category):
    if category == "physical":
        return "Generate a physical health suggestion."
    elif category == "mental":
        return "Generate a mental health suggestion."


@app.route("/")
def index():
    return render_template("index.html")


def get_completion(prompt, model="gpt-3.5-turbo"):
    print(prompt)
    prompt_answer = f"""
        Perform the following actions:
        "You are a consultant providing health suggestions. 
        Always give me a new suggestion.",

        ```{prompt}```
    """
    messages = [{"role": "user", "content": prompt_answer}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # the degree of randomness of the model's output
    )
    random_choice_index = random.randint(0, len(response.choices) - 1)
    return response.choices[random_choice_index].message["content"]


@app.route("/generate", methods=["POST"])
def generate():
    global last_request_time

    # Check if enough time has passed since the last request
    current_time = time.time()

    # Use request.form.get to handle potential BadRequestKeyError
    category = request.form.get("category")
    print(category)

    if not category:
        return jsonify({"error": "Category is missing in the form data."}), 400

    prompt = generate_prompt(category)

    # Use the new OpenAI interface
    response = get_completion(prompt)

    # Update the last_request_time after a successful request
    last_request_time = current_time

    # Update the return statement in your generate function
    return jsonify({"generated_text": response})


if __name__ == "__main__":
    app.run(debug=True)
