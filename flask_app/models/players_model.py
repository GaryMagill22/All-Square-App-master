import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Player:
    DB = "all_square_schema_updated"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.username = data['username']
        self.password = data['password']
        self.handicap = data['handicap']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_player(newPlayer):
        is_valid = True  # we assume this is true
        if len(newPlayer['first_name']) < 2:
            flash("First Name is required.")
            is_valid = False

        if len(newPlayer['last_name']) < 2:
            flash("Last Name is required.")
            is_valid = False

        if len(newPlayer['email']) < 3:
            flash("Email must be a valid email address")
            is_valid = False

        if len(newPlayer['username']) < 3:
            flash("username must be a valid username")
            is_valid = False

        if len(newPlayer['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if len(newPlayer['confirm_password']) < 8:
            flash("Passwords must match.")
            is_valid = False
        return is_valid

    @classmethod
    def create_player(cls, data):
        query = """
        INSERT INTO players (first_name, last_name, email, username, password, handicap)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(username)s, %(password)s, 25);
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    @classmethod
    def get_player_by_id(cls, data):
        query = """
        SELECT * FROM players
        WHERE id = %(player_id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM players WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])
