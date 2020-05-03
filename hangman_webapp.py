"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

global state
state = {'guesses':[],
         'word':"interesting",
		 'word_so_far':"-----------",
		 'done':False
		 }
completeCheck = []
for i in state['word']:
	completeCheck.append('-')


@app.route('/')
@app.route('/main')
def main():
	return render_template('hangman.html')

@app.route('/start')
def play():
	global state
	state['word']=hangman_app.generate_random_word()
	state['guesses'] = []
	return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
	""" plays hangman game """
	global state
	if request.method == 'GET':
		return play()

	elif request.method == 'POST':
		letter = request.form['guess']
		if letter in state['guesses']:
			print("You already guessed that letter. Try again.")
		elif letter in state['word']:
			for i in state['word']:
				if i == letter:
					position = state['word'].index(letter)
					completeCheck[position] = letter
					tempCheck = "".join(completeCheck)
					state['word_so_far'][position] = letter
					if tempCheck == state['word']:
						print("you win")
		state['guesses'] += [letter]
		return render_template('play.html',state=state)

@app.route('/minsung-page')
def minsung():
	return render_template('minsung.html')

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0',port=3000)

