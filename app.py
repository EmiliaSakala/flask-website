from enum import unique
from flask import Flask, render_template, request
from form import LoginForm
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")




app =  Flask(__name__)
app.config['SECRET_KEY'] = 'emisecretkey'
 

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/contact')
def hello():
    return "<h1>Our Contact Page</h1>"

@app.route('/user/<name>')
def User(name):
    return "<h1>Welcome Miss. {}</h1>".format(name)

@app.route('/login', methods = ['GET', 'POST'])
def Login():
    form = LoginForm()

  
    return render_template('login.html', title = 'Login', form=form)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)