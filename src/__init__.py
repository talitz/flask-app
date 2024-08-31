import logging

import requests
from flask import Flask, jsonify

from src.authentication import create_basic_authentication
from src.database import init_and_fill_db, query_db
from src.rate_limit import create_limiter


def create_flask_app():
    app_ret = Flask(__name__)
    init_and_fill_db()
    basic_auth_ret = create_basic_authentication(app_ret)
    limiter_ret = create_limiter(app_ret)
    return app_ret, basic_auth_ret, limiter_ret


app, basic_auth, limiter = create_flask_app()


## This part should be externalized to routes.py
@app.route('/')
@limiter.limit("2 per day")
def hello():
    return 'Hi there!'


@app.route('/json')
@limiter.limit("5 per minute")
def get_json():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    return jsonify(response.json())


@app.route('/json/user/<int:user_id>', methods=['GET'])
@basic_auth.required
@limiter.limit("5 per minute")
def get_user(user_id):
    try:
        query = "SELECT * FROM users WHERE userId = {}".format(user_id)
        user = query_db(query)
        logging.getLogger().info(f"Query result: {user}")
        if user:  # If user is found, return the data as JSON
            return jsonify(user), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        logging.getLogger().error(f"An exception occurred in /json/user/{user_id}: {repr(e)}")
        return jsonify({"error": "An internal error occurred"}), 500


# Health check
@app.route('/health', methods=['GET'])
@limiter.limit("3000 per minute")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
