from flask import Blueprint, request
from service import user_service

user_route = Blueprint("user_route", __name__)


@user_route.route("/api/v1/islam/user", methods=["GET"])
def get_user():
    return user_service.get_user(request)

@user_route.route("/api/v1/islam/user", methods=["POST"])
def post_user():
    return user_service.post_user(request)
