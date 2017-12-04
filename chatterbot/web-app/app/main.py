from flask import Flask, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

bot = ChatBot("English Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

bot.set_trainer(ChatterBotCorpusTrainer)
bot.train(
    "chatterbot.corpus.english",
    "./excella/"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get/<string:query>")
def get_raw_response(query):
    return str(bot.get_response(query))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)