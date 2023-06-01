from flask_app import app
from flask_app.controllers import players_controller, games_controller, courses_controller


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)
