from  flask import Flask,  jsonify

app = Flask(__name__)

@app.route('/orders')
def orders():
	return jsonify([
		{"id": 101, "produto": "Notebook", "valor": 3500.00},
		{"id": 102, "produto": "Mouse", "alor": 90.00}
	])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

