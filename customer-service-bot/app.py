import os
from flask import Flask, request, render_template, jsonify
import logging
import openai

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/generate', methods=['POST'])
def generate():
    # the textarea is sent in form data format
    data = request.form['text']
    # for local testing
    # data = request.get_json()['text']
    result = get_customer_service_response(data)
    return jsonify(result)


def extract_content_from_response(response) -> str:
    return response['choices'][0]['message']['content']


def format_prompt(review):
    text_body = """
    Extract the sentiment and generate a reply to the following customer review. 
    The sentiment should be only in 3 kinds <negative, neutral, positive>. 
    Return the response in json format, with sentiment and response as keys. For example

    {{
       sentiment: positive,
       response: Thanks for your review!
    }}
    ---
    {review}
    ---

        """
    return text_body.format(review=review)


def get_customer_service_response(review: str) -> str:
    prompt = format_prompt(review)
    app.logger.info(prompt)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a customer service that is patient and nice"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )
    app.logger.info('Request successful')
    content = extract_content_from_response(response)
    app.logger.info(content)
    return content


if __name__ == '__main__':
    app.run(debug=True, load_dotenv=True)
