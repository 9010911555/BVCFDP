import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def grade_from_percentage(pct: float) -> str:
	if pct >= 90:
		return "A+"
	if pct >= 80:
		return "A"
	if pct >= 70:
		return "B"
	if pct >= 60:
		return "C"
	if pct >= 50:
		return "D"
	return "F"


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
	# Expect marks sent as marks[] from the form
	marks_raw = request.form.getlist('marks[]')
	try:
		marks = [float(m) for m in marks_raw if m != '']
	except ValueError:
		return "Invalid marks provided.", 400

	if not marks:
		return redirect(url_for('index'))

	total = sum(marks)
	num = len(marks)
	max_total = num * 100.0
	percentage = (total / max_total) * 100.0
	grade = grade_from_percentage(percentage)

	return render_template('result.html', marks=marks, total=total, num=num, percentage=round(percentage, 2), grade=grade)


if __name__ == '__main__':
	app.run(debug=True)

