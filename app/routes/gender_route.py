from flask import Blueprint
from app.controllers.gender_controller import get_gender

gender_blueprint = Blueprint('gender', __name__)

gender_blueprint.route("/gender", methods=["GET"])(get_gender)
