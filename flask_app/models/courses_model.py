from flask_app import app
from flask import render_template, redirect, request, session, flash
# from flask_app.models.games_model import Game
from flask_app.config.mysqlconnection import connectToMySQL


class Course:
    DB = "all_square_schema_updated"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.course_index = data['course_index']
        self.slope_index = data['slope_index']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_courses(cls):
        query = """
        SELECT * FROM courses 
        """
        result = connectToMySQL(cls.DB).query_db(query)

        all_courses = []

        for row in result:
            all_courses.append(Course(row))
        return all_courses

    @classmethod
    def get_course_by_id(cls, data):
        query = """
        SELECT * FROM courses
        WHERE id = %(course_id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])
