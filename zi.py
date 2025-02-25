from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# プレイヤーの状態を保存する辞書（プレイヤーIDをキーとして使用）
players = {}

@app.route('/register', methods=['POST'])
def register_player():
    # 新しいプレイヤーを登録する
    player_id = str(uuid.uuid4())  # ユニークなプレイヤーIDを生成
    players[player_id] = {'position': (0, 0, 0)}  # 初期位置
    return jsonify({'id': player_id})

@app.route('/player/<player_id>', methods=['GET'])
def get_player(player_id):
    # プレイヤーの位置を取得
    player = players.get(player_id)
    if player:
        return jsonify(player)
    else:
        return jsonify({'error': 'Player not found'}), 404

@app.route('/player/<player_id>', methods=['PUT'])
def update_player(player_id):
    # プレイヤーの位置を更新
    data = request.json
    if player_id in players:
        players[player_id]['position'] = data['position']
        return jsonify({'message': 'Player position updated'})
    else:
        return jsonify({'error': 'Player not found'}), 404

@app.route('/players', methods=['GET'])
def get_all_players():
    # すべてのプレイヤーの情報を取得
    return jsonify(players)

if __name__ == '__main__':
    app.run(debug=True)
