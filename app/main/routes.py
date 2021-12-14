from flask import render_template, url_for, request, jsonify, current_app
from app.main import bp


@bp.route('/', defaults={"path":""})
def serve(path):
    return render_template("index.html")