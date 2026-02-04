from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Handle AutoResponder requests here
    response = {'status': 'success', 'message': 'Webhook received.'}
    return jsonify(response), 200

@app.route('/register', methods=['POST'])
def register():
    player_data = request.json
    # Implement registration logic for kingdoms game
    # Save player_data to database or variable
    response = {'status': 'success', 'message': 'Player registered successfully.'}
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)