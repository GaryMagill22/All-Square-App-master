import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


#  MODEL USED TO STORE ALL GAMES

class Game_Info:
    DB = "all_square_schema_updated"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.min_players = data['min_players']
        self.max_players = data['max_players']
        self.rules = data['rules']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# GETS ALL GAMES IN THE DATABASE


    @classmethod
    def get_all_game_info(cls):
        query = """
        SELECT * FROM games_info 
        """
        result = connectToMySQL(cls.DB).query_db(query)

        all_game_info = []

        for row in result:
            all_game_info.append(cls(row))
        return all_game_info
