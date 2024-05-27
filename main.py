from flask import Flask, render_template, request, session, redirect, url_for
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session encryption

def initialize_game():
    session['chambers'] = [False] * 5
    bullet_position = random.randint(0, 4)
    session['chambers'][bullet_position] = True
    session['attempts'] = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'chambers' not in session:
        initialize_game()
    
    if request.method == 'POST':
        chambers = session['chambers']
        session['attempts'] += 1

        if chambers:
            current_chamber = chambers.pop(0)  # Remove the first chamber
            if current_chamber:
                result = "You are dead!"
                session.pop('chambers', None)  # Reset game
            else:
                result = "Click! You survived!"
        else:
            result = "No more chambers left! Game over!"
            session.pop('chambers', None)  # Reset game

        return render_template('index.html', result=result, attempts=session['attempts'])
    
    return render_template('index.html', result=None, attempts=session.get('attempts', 0))

if __name__ == '__main__':
    app.run(debug=True)
