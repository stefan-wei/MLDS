from flask import Flask, render_template, request
import pickle


app = Flask(__name__)
app.static_folder = 'static'


@app.route('/')
def index():
	title = "Simulation for Preventative Intervention of Diabetic Risk"
	return render_template("index.html", title=title)

@app.route('/results', methods=["POST"])
def results():
	bmi = request.form.get("bmi")
	age = request.form.get("age")
	glucose = request.form.get("glucose")
	bp = request.form.get("bp")
	Pkl_Filename = "newmodel.pkl"
	with open(Pkl_Filename, 'rb') as file:
	    model = pickle.load(file)
	ptdata = [[glucose, bp, bmi, age]]
	result = model.predict_proba(ptdata)[:,1]
	result = result[0]
	result = result * 100
	float_str = float(result)
	result = int(float_str)

	title = "Simulation for Preventative Intervention of Diabetic Risk"
	return render_template("results.html", title=title, bmi=bmi, age=age, glucose=glucose, bp=bp, result=result)

@app.route('/ai')
def ai():
	title = "Behind the AI"
	return render_template("ai.html", title=title)

@app.route('/learn', methods = ['GET', 'POST'])
def learn():
	title = "Learning Resources"
	return render_template("learn.html", title=title)
