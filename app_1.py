from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded token for simplicity
TOKEN = "MySecretToken" 

# In-memory storage for todos
todos = [] 

# Middleware: Token authentication check -> this run before every request
@app.before_request
def authenticate_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401

# GET endpoint to fetch all todo items
@app.route("/todos", methods=["GET"]) 
def get_todos():
    return jsonify(todos), 200

# POST endpoint to create a todo item
@app.route("/todos", methods=["POST"]) 
def create_todo():
    if not request.json or "title" not in request.json:
        return jsonify({"error": "Bad Request, title is missing"}), 400
    todo = {
        "id": len(todos) + 1,
        "title": request.json.get("title"),
        "completed": request.json.get("completed", False),
    }
    todos.append(todo)
    return jsonify(todo), 201

# PUT endpoint to update an existing todo item by id
@app.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id): 
    todo = next((t for t in todos if t["id"] == id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    todo["title"] = request.json.get("title", todo["title"])
    todo["completed"] = request.json.get("completed", todo["completed"])
    return jsonify(todo), 200

# DELETE endpoint to remove an existing todo item by id
@app.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id): 
    global todos
    todos = [t for t in todos if t["id"] != id]
    return '', 204

# GET endpoint for a specific todo item by id
@app.route("/todos/<int:id>", methods=["GET"])
def get_todo_by_id(id): 
    todo = next((t for t in todos if t["id"] == id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify(todo), 200

# DELETE endpoint to clear all todo items
@app.route("/todos", methods=["DELETE"])
def clear_all_todos():
    global todos
    todos.clear()  
    return jsonify({"message": "All todos have been cleared."}), 200


# 404 handler for unknown routes
@app.errorhandler(404)
def not_found(e): 
    return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)
 