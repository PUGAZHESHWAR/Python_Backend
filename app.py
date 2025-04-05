from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Expected username and password
EXPECTED_USERNAME = "admin"
EXPECTED_PASSWORD = "admin"

@app.route('/authenticate/admin', methods=['POST'])
def login():
    # Get JSON data from the request
    client_ip = request.remote_addr
    print(f"Request made from IP: {client_ip}")
    data = request.get_json()
    
    # Validate the username and password
    if data.get('username') == EXPECTED_USERNAME and data.get('password') == EXPECTED_PASSWORD:
        return jsonify({"jwt": "Data is valid"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
