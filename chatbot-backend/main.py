from flask import Flask, request, jsonify, render_template
from decouple import config
import openai
app = Flask(__name__)

openai.api_key=config("api_key")
# Configure Chatbot Parameters
# temperature = 0.7
# max_tokens = 50
# stop_sequence = "\n"



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("user_input")
    print("Received user_input:", user_input) 
    # Initialize a conversation with a system message
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]
    # Continue the conversation with the user's message
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=50  # Adjust as needed
    )

    # Extract the chatbot's response
    chatbot_response = response.choices[0].message["content"]

    return jsonify({"chatbot_response": chatbot_response})

if __name__ == "__main__":
    app.run(debug=True)