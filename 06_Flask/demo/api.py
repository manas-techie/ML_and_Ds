# put and delete - HTTPS verbs
# working with apis - JSONs

from flask import Flask, jsonify, request

app = Flask(__name__)

# intial data is my todo list
items = [
    {"id": 1, "task": "Buy groceries", "description": "Milk, Bread, Eggs"},
    {"id": 2, "task": "Clean the house", "description": "Vacuum, mop, dust"},
    {"id": 3, "task": "Finish the project", "description": "Complete the final report"}
]


@app.route('/')
def home(): 
    return "Welcome to the To-Do List API!"


# GET: Retrive all items in the list
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET: Retrive a specific item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item: 
        return jsonify(item)
    else: 
        return jsonify({"error": "Item not found"}), 404

# POST: Add a new item to the list
@app.route('/items', methods=['POST'])
def add_item():
    if not request.json or 'task' not in request.json:
        return jsonify({"error": "Task is required"}), 400
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "task": request.json['task'],
        "description": request.json.get('description', "") 
        # "description: request.json['description']
    }

    items.append(new_item)
    return jsonify(new_item), 201

# PUT: Update an existing item

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item: 
        return jsonify({"error": "Item not found"}), 404 
    item['task'] = request.json.get('task',item['task'])
    item['description'] = request.json.get('description',item['description'])
    return jsonify(item)


# DELETE: Remove an item from the list
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item is deleted"})



if __name__ == "__main__":
    app.run(debug=True)

