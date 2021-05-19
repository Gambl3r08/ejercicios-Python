import json
from flask import Flask, jsonify
from flask.globals import request

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return jsonify({'name': 'rj', 'email':'robertojoselozada@gmail.com'})

@app.route('/datos', methods=['GET'])
def datos():
    return jsonify({'dato': "dato de prueba"})

@app.route('/datos', methods=['POST'])
def postDatos():
    record = json.loads(request.data)
    with open('data.txt', 'r') as f:
        data = f.read()
        if not data:
            records = [record]
        else:
            records = json.loads(data)
            records.append(record)
        with open('data.txt', 'w') as f:
            f.write(json.dumps(records, indent=2))
        return jsonify(record)


app.run()