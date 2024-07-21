from flask import Flask, request, render_template
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

class NLTKChatbot:
    def __init__(self):
        self.pairs = [
            ['need help', ['How can I help you?']],
            ['What is BHR ?', ['BHR stands for Basic Human Rights']],
            ['Other', ['How can I help you?']],
            ['How are you How’s it going?', ['How are you doing, What’s up']],
            ['Are you a robot?', ['Yes, I’m a robot but I’m a smart one!']]
        ]
        self.chat = Chat(self.pairs, reflections)

    def respond(self, message):
        return self.chat.respond(message)

chatbot = NLTKChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_response = chatbot.respond(user_message)
    return bot_response

if __name__ == '__main__':
    app.run(debug=True)
