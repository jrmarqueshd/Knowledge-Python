from flask import Flask, jsonify, request

from modules.users import Users as users
from modules.calculator import Calculator as calculator
from helpers.services import JSONHelpers as jsonhelpers

app = Flask(__name__) 

@app.route('/get-users')
def get_users():
  return users().getusersinfo()

@app.route('/save-users', methods=['POST'])
def save_users():
  jsonhelpers("assets/newusers").save(users().getusersinfo())
  return jsonify({"success": True, "message": "Users saved with success.", "status": 200}), 200

@app.route('/calculator', methods=['POST'])
def calculator_exec():
  # jsonhelpers("assets/newusers").save(users().getusersinfo())
  operator = request.get_json()['operator']
  a = request.get_json()['a']
  b = request.get_json()['b']

  result = calculator(operator, a, b).exec()

  return jsonify({
    "a": a, 
    "b": b, 
    "operator": operator, 
    "result": int(result)
  }), 200


# @app.route('/hello', methods=['POST', 'GET'])
# def hello():
#   request.get_json()
#   return '', 204

if __name__ == '__main__':
    app.run(debug=True) 