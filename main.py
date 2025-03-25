import flask
import re


# TODO: change this to your academic email
AUTHOR = "syensi@seas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    # FIXME: to be implemented
    if len(pw) < 8:
        return flask.jsonify({"valid": False, "reason": "Password too short"}), 400
    if len(re.findall(r"[A-Z]", pw)) < 2:
        if re.search(r"[A-Z]", pw):
            return flask.jsonify({"valid": False, "reason": "Not enough uppercase letter"}), 400
        else:
             return flask.jsonify({"valid": False, "reason": "Missing uppercase letter"}), 400
    if len(re.findall(r"[a-z]", pw)) < 2:
        if re.search(r"[a-z]", pw):
            return flask.jsonify({"valid": False, "reason": "Not enough lowercase letter"}), 400
        else:
             return flask.jsonify({"valid": False, "reason": "Missing lowercase letter"}), 400
    if not re.search(r"[0-9]", pw):
        return flask.jsonify({"valid": False, "reason": "Missing digit"}), 400
    if not re.search(r"[!@#$%^&*]", pw):
        return flask.jsonify({"valid": False, "reason": "Missing special character"}), 400

    return flask.jsonify({"valid": True, "reason": "Password is strong"}), 200