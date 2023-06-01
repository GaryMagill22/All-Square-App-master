from flask_app import app
from flask import render_template, redirect, request, session, flash
# have to import the course model here
from flask_app.models.courses_model import Course
from flask_app.models.games_info_model import Game_Info
from flask_app.models.games_model import Game
from flask_app.models.players_rounds_model import Players_Round
# from flask_app.models.players_model import Player


# ================================================


@app.route('/courses')
def get_all_courses():

    if "players_id" not in session:
        return redirect('/')
    # ".get_all_rcourses" has to match classmethod exactly for Course class"
    courses_info = Course.get_all_courses()

    return render_template('courses.html', courses_info=courses_info)
# take the courses_info (where stored info) and passing it into the html page to display using jinja to parse it.

# ================================================


@app.route('/courses/<int:course_id>')
def course_in_session(course_id):
    session['chosen_course'] = course_id
    # print(session['chosen_course'])
    return redirect('/choose_game')


#  ONCE game ends MAKE SURE TO CLEAR OUT CHOSEN_SELECTIONS
# session.pop('chosen_course)
# session.pop('chosen_game)
# session.pop('chosen_num_of_players)

# ================================================

@app.route('/choose_course')
def choose_course():
    courses_info = Course.get_all_courses()
    games_info = Game_Info.get_all_game_info()
    # Populating dropdown options
    # print(games_info)
    return render_template('choose_course.html', games_info=games_info, courses_info=courses_info)


# ================================================
