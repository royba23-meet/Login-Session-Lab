from flask import Flask, render_template, request, url_for, redirect
from flask import session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
quotes={}

@app.route('/', methods=['POST', 'GET']) # What methods are needed?
def home():
	session['logged'] = False
	if request.method == 'POST':
		try:
			if len(request.form['username']) <= 0 or len(request.form['quote']) <= 0 or len(request.form['age']) <= 0: #Very disgusting triple or statement but it works
				raise(ValueError)
			session['username'] = request.form['username']
			session['quote'] = request.form['quote']
			session['age'] = request.form['age']
			session['logged'] = True
			quotes[session['username']] = session['quote']
			return redirect(url_for('thanks'))	
		except ValueError:
			return redirect(url_for('error'))
	return render_template('home.html')


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():
	if 'logged' in session and session['logged']:
			return render_template('display.html', username=session['username'], quote=session['quote'], age=session['age'])
	return redirect(url_for('home'))


@app.route('/thanks')
def thanks():
	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)