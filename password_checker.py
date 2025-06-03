from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include uppercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include special characters.")

    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong 🔐"
    elif score == 3:
        strength = "Moderate ⚠️"
    elif score == 2:
        strength = "Weak 🚫"
    else:
        strength = "Very Weak ❌"

    return strength, feedback

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None
    feedback = []
    password = ""

    if request.method == 'POST':
        password = request.form['password']
        strength, feedback = check_password_strength(password)

    return render_template('index.html', strength=strength, feedback=feedback, password=password)

if __name__ == '__main__':
    app.run(debug=True)