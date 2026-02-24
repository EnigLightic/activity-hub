from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # 基础校验
    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    # 检查邮箱是否存在
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400

    # 检查用户名是否存在
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already taken"}), 400

    # 创建用户
    user = User(
        username=username,
        email=email,
        password=password  # 现在先不加密
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        }
    }), 201