from flask import Flask, request, abort, jsonify

app = Flask(__name__)

# Predefined password for authentication
VALID_PASSWORD = "secure_password"

@app.route('/login', methods=['POST'])
def login():
    # Get the password from the request
    data = request.json
    if not data or 'password' not in data:
        abort(400)

    password = data['password']

    # Check if the password is valid
    if password != VALID_PASSWORD:
        abort(401)

    # If password is valid, return success message
    return jsonify({"message": "Login successful!"})

# Custom error handler for 401 Unauthorized
@app.errorhandler(401)
def unauthorized_error(e):
    return jsonify({"error": str(e)}), 401

# Custom error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request_error(e):
    return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
