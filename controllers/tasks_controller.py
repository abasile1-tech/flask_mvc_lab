from flask import Blueprint

tasks_blueprint = Blueprint("tasks", __name__)

@tasks_blueprint.route("/tasks")
def index():
	return "<h1>Tasks be here</h1>"