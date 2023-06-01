import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Players_Round:
    DB = "all_square_schema_updated"

    def __init__(self, data):
        self.id = data['id']
        self.player_id = data['player_id']
        self.game_id = data['game_id']
        self.hole_num = data['hole_num']
        self.score = data['score']
        self.outcome = data['outcome']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_round_info(cls, data):
        query = """
        SELECT * FROM players_rounds
        WHERE id = %(player_id)s, %(game_id)s;
        """

        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def add_round(cls, data):
        query = """
        INSERT INTO players_rounds (player_id, game_id, hole_num, score, outcome)
        VALUES ( %(player_id)s, %(game_id)s, %(hole_num)s, %(score)s, %(outcome)s )
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    # @classmethod
    # def get_players_from_database(cls, hole_num):
    #     query = """
    #     SELECT * FROM players_rounds
    #     WHERE id = %(player_id)s AND game_id = %(game_id)s;
    #     """

    #     result = connectToMySQL(cls.DB).query_db(query, hole_num)
    #     return result
