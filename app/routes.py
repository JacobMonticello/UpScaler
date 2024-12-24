from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Flask API!"})
