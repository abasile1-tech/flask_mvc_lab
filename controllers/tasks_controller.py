from flask import Blueprint, render_template

tasks_blueprint = Blueprint("tasks", __name__)

@tasks_blueprint.route("/tasks")
def index():
	return render_template("index.html", title="My Task List")