from nltk.chat.util import Chat, reflections

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

# Usage:
# chatbot = NLTKChatbot()
# response = chatbot.respond("hello")
# print(response)
