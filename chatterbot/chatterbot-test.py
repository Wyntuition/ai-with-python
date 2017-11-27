from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# # Train based on english greetings corpus
# chatbot.train("chatterbot.corpus.english.greetings")

# # Train based on the english conversations corpus
# chatbot.train("chatterbot.corpus.english.conversations")

# # Get a response to an input statement
# print(chatbot.get_response("Hello, how are you today?"))

# The following loop will execute each time the user enters input
while True:
    try:
        response = chatbot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break