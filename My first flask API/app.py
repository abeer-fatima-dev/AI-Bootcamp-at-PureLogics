from flask import Flask, request, jsonify
from storage import todos

app = Flask(__name__)

# Home
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to my first Flask Application!"
    })

# About
@app.route("/about", methods=["GET"])
def about():
    return jsonify({
        "message": "This is my first Flask Bootcamp Project"
    })

# Get all todos
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

# Get todo by ID
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):

    for todo in todos:
        if todo["id"] == todo_id:
            return jsonify(todo)

    return jsonify({"message": "Todo not found"}), 404

# Create todo
@app.route("/todos", methods=["POST"])
def create_todo():

    data = request.get_json()

    if not data or "task" not in data:
        return jsonify({"message": "Task is required"}), 400

    todo = {
        "id": len(todos) + 1,
        "task": data["task"]
    }

    todos.append(todo)

    return jsonify({
        "message": "Task added successfully",
        "todo": todo
    }), 201

# Update todo
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):

    data = request.get_json()

    for todo in todos:
        if todo["id"] == todo_id:

            todo["task"] = data["task"]

            return jsonify({
                "message": "Todo updated successfully",
                "todo": todo
            })

    return jsonify({"message": "Todo not found"}), 404

# Delete todo
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):

    for todo in todos:
        if todo["id"] == todo_id:

            todos.remove(todo)

            return jsonify({
                "message": "Todo deleted successfully"
            })

    return jsonify({"message": "Todo not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
