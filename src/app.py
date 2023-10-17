from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text 

@app.route('/todos', methods=['POST'])
def add_new_todo():
    decode = request.get_json()
    print("Incoming request with the following body", decode)
    todos.append(decode)
    json_text = jsonify(todos)
    return json_text 


@app.route('/todos/<int:position>',methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete", position)

    longitud= len(todos) 
    print("longitud:", longitud)

    maxIndex= longitud-1

    if position> maxIndex:
        return jsonify({"message":"el numero es mayor de la cantidad de elementos"},400)
    elif longitud == 0:
        return jsonify({"message":"La lista esta vacia, y por eso maxIndex"},400)

    todos.pop(position)

    json_text = jsonify(todos)
    return json_text










if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)