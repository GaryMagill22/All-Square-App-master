from flask_bcrypt import Bcrypt
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.players_model import Player
from flask_app.models.games_model import Game
app.secret_key = 'secretkey'

bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return render_template('register_login.html')

# =================================================


@app.route('/player/profile')
def show_profile():
    return render_template('profile.html')

# =================================================


@app.route('/register_player', methods=['POST'])
def register_player():

    if not Player.validate_player(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    register_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'username': request.form['username'],
        'email': request.form['email'],
        'password': pw_hash
    }
    player_id = Player.create_player(register_data)
    session['player_id'] = player_id
    session['first_name'] = request.form['first_name']
    session['username'] = request.form['username']
    return redirect("/dashboard")
# redirect matches the success route

# =================================================


@app.route('/login_player', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = {"email": request.form["email"]}
    player_in_db = Player.get_by_email(data)
    # user is not registered in the db
    if not player_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(player_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the player_id into session
    # print('=====================>PLAYER_IN_DB: ', player_in_db)
    session['players_id'] = player_in_db.id
    session['username'] = player_in_db.username
    # never render on a post!!!
    return redirect('/dashboard')


# =================================================


@app.route('/dashboard')
def successful_login():

    if 'player_id' not in session:
        return redirect('/')
    # if session['user_id'] != user_id:
    #     return redirect('/')
    # new_user = User.GetUserById({'user_id': user_id})
    return render_template('dashboard.html')

# ====================================


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# ====================================
#    Create Routes
#    Show Form Route, Submit(action) Form Route
# route to show form (render form). route to submit form(post route)
# ====================================
#
# ====================================
#    Read Routes
#    Show Routes (Get All and Get One)
#  route to render template (No post route)
# ====================================
# ====================================
#    Update Routes
#    Update Form Route, Submit Update Form Route
# route to show form (render form). route to update/edit(post route)
# ====================================
# ====================================
#    Delete Routes
# ====================================
