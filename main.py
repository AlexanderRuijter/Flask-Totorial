from flask import Flask, render_template, request

loginCheck = False

Smash_versions = ["Smash", "HarderSmash", "EvenHarderSmash", "!SMASH!"]

# Create a flask app
app = Flask(__name__,
  template_folder='templates',
  static_folder='static'
)

@app.route('/login/')
def test():
  return render_template('loginPage.html')
username = []
passwords = []

# Index page (now using the index.html file)
@app.route('/HomePage/', methods=['POST'])
def login():
 username = request.form['username']
 password = request.form["password"]
 return render_template('homePage.html', 
 username = username, password = password)


@app.route ("/game1")
def game1():
  return render_template("game1.html")
@app.route ("/HomePage/")
def HomePage():
  return render_template("homePage.html")
@app.route ("/games/")
def games():
  return render_template("games.html")
@app.route("/")
def main():
  return render_template('mainPage.html')
@app.route("/Pass/11010011/ilgalMoney/")
def ilgalMoney():
  return render_template("ilegalMoney.html")


if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )