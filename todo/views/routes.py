from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

# 1. 获取所有待办事项
@api.route('/todos', methods=['GET'])
def get_todos():
    return jsonify([{
        "id": 1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    }])

# 2. 获取指定 ID 的待办事项
@api.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    return jsonify({
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    })

# 3. 创建新的待办事项
@api.route('/todos', methods=['POST'])
def create_todo():
    return jsonify({
        "id": 1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    }), 201

# 4. 更新指定 ID 的待办事项
@api.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    return jsonify({
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    })

# 5. 删除指定 ID 的待办事项
@api.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    return jsonify({
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    })


@api.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

