from flask import Blueprint

bp = Blueprint('android', __name__, url_prefix='/android')

@bp.route('/', methods=["POST"])
def crate_images():
    pass 