from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.games_info_model import Game_Info
from flask_app.models.games_model import Game
from flask_app.models.courses_model import Course
from flask_app.models.players_rounds_model import Players_Round
# from flask_app.models.players_model import Player


@app.route('/games')
def games():
    return render_template('games.html')


@app.route('/games/wolf')
def wolf():
    return render_template('wolfGame.html')


# ==============================================
@app.route('/games/wolf/show')
def show_wolf_game():
    return render_template('wolfGame.html')

# ==============================================


@app.route('/choose_game')
def choose_game():
    courses_info = Course.get_all_courses()
    games_info = Game_Info.get_all_game_info()
    # Populating dropdown options
    print(games_info)
    return render_template('choose_game.html', games_info=games_info, courses_info=courses_info)


# ===============================================
@app.route('/games/<int:game_id>')
def game_in_session(game_id):
    session['chosen_game'] = game_id

    # print(session['chosen_game'])
    return redirect('/setup_round')

#  ONCE game ends MAKE SURE TO CLEAR OUT CHOSEN_SELECTIONS
# session.pop('chosen_course)
# session.pop('chosen_game)
# session.pop('chosen_num_of_players)
# ===============================================


@app.route('/setup_round')
def setup_round():
    chosen_game = Game.get_game_by_id(
        {"games_id": session['chosen_game']})
    chosen_course = Course.get_course_by_id(
        {"course_id": session['chosen_course']})
    return render_template('setup_round.html', chosen_course=chosen_course, chosen_game=chosen_game)


# ===============================================

# @app.route('/play_game', methods=['POST'])
# def play_game():

#     # if not Game.validate_game(request.form):
#     #     return redirect('')

#     game_data = {
#         'course_id': session['chosen_course'],
#         'game_info_id': session['chosen_game'],
#         # 'hole_num': session['hole_num'],
#         'players': get_players_from_database()
#     }

#     game_data = Game.play_game(game_data)
#     return render_template('hole.html')

# ===============================================


@app.route('/play_game/', methods=['POST'])
def play_game():
    # Retrieve the current hole number from the query parameters or default to 1
    hole_num = int(request.args.get('hole_num', 1))

    # Set the 'hole_num' value in the session
    session['hole_num'] = hole_num

    # Retrieve the players' data from the database (e.g., names and scores)
    players = get_players_from_database()

    return render_template('hole.html', hole_num=hole_num, players=players)

# ===============================================

# Common HTML template for all holes


@app.route('/play_game/<int:hole_num>', methods=['GET', 'POST'])
def score_hole(hole_num):
    if request.method == 'POST':
        # Retrieve the submitted scores and save them in the database

        # Redirect to the next hole or a completion page

        if hole_num+1 <= 18:
            return redirect(f'/play_game/{hole_num}')
        else:
            return render_template('completion.html')
    else:
        # Retrieve the players' data from the database (e.g., names)
        players = get_players_from_database()

        hole_data = {
            **request.form,
            'hole_num': ['hole_num + 1'],
            'player_id': ['player_id'],
            'score': ['score']

        }
    return render_template('hole.html', hole_num=hole_num, players=players, **request.form)

# Utility function to retrieve players from the database


def get_players_from_database():
    # Retrieve the player data from the database and return it
    return []


# ===============================================

@app.route('/test_score/<int:hole_num>', methods=['POST'])
def test_score(hole_num):
    print(request.form)
    # all_playerscore_data = []
    # All data from the form, put into an array
    all_playerscore_data = [
        # Player 1 Data
        {
            'player_id': request.form['player1_id'],
            'game_id': ['game_id'],
            'hole_num': ['hole_num'],
            'score': request.form['player1Score'],
            'outcome': 'won'
        },
        # Player 2 Data
        {
            'player_id': request.form['player2_id'],
            'game_id': ['game_id'],
            'hole_num': ['hole_num'],
            'score': request.form['player2Score'],
            'outcome': 'loss'
        },
        # Player 3
        {
            'player_id': request.form['player3_id'],
            'game_id': ['game_id'],
            'hole_num': ['hole_num'],
            'score': request.form['player2Score'],
            'outcome': 'loss'
            # Player 4
        },
        {

            'player_id': request.form['player4_id'],
            'game_id': ['game_id'],
            'hole_num': ['hole_num'],
            'score': request.form['player2Score'],
            'outcome': 'loss'
        },
    ]

    for player in all_playerscore_data:
        Players_Round.add_round(player)

    return redirect(f'/play_game/{hole_num+1}')
# ===============================================
