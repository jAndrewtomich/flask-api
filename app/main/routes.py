from flask import current_app
from flask.helpers import send_from_directory
from app.main import bp


@bp.route('/', defaults={"path":""})
def serve(path):
    return send_from_directory(current_app.static_folder, "index.html")