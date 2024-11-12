from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index2.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    gender = request.form.get('gender')
    if username:
        # Redirects to the login_details route, passing username and gender in the URL
        return redirect(url_for('login_details', username=username, gender=gender))
    return redirect(url_for('index'))

@app.route('/login_details/<username>/<gender>')
def login_details(username, gender):
    # Renders the login_details page with the username and gender
    return render_template('login_details.html', username=username, gender=gender)

if __name__ == '__main__':
    app.run(debug=True)
