from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def hello():
  if request.method == 'POST':
    return request.get_json()
  
  return jsonify({"hello": "world"})

if __name__ == '__main__':
    app.run(debug=True) 