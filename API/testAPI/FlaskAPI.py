from flask import Flask, jsonify, request

app = Flask(__name__)

# 实例数据
data = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Cathy'}
]

# 获取所有数据
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

# 根据ID获取单个数据
@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(data_id):
    item = next((item for item in data if item ['id'] == data_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'data not found'}), 404
    
# 添加新数据
@app.route('/data', methods=['POST'])
def add_data():
    new_item = request.get_json()
    data.append(new_item)
    return jsonify(new_item), 201

# 更新数据
@app.route('/data/<int:data_id>', methods=['POST'])
def update_data(data_id):
    item = next((item for item in data if item['id'] == data_id), None)
    if item:
        update_item = request.get_json()
        item.update(update_item)
        return jsonify(item)
    else:
        return jsonify({'error': 'Data not found'}), 404
    
#  删除数据
@app.route('/data<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    global data
    data = [item for item in data if item['id'] != data_id]
    return jsonify({'message': 'Data deleted'})

if __name__ == '__main__':
    app.run(debug =True)