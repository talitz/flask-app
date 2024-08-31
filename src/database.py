import logging
import sqlite3

import requests

from src.utils import get_relative_db_path

DATABASE = get_relative_db_path("../db/flask_app.db")

def create_connection(db=DATABASE):
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()  # Create a cursor object to interact with the database
        if cursor is not None:
            return (cursor, conn)
    except Exception as e:
        logging.getLogger().error("An exception occurred while connecting to DB: {}".format(db), repr(e))


def commit_and_close_connection(cursor, connection):
    try:
        connection.commit()
        cursor.close()  # Commit the changes and close the connection
        connection.close()
    except Exception as e:
        logging.getLogger().error("An exception occurred while closing the DB connection", repr(e))


def init_and_fill_db():
    (cursor, conn) = create_connection()
    try:
        logging.info("Creating DB users table")
        # Create the 'users' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                completed BOOLEAN NOT NULL,
                userId INTEGER
            );
        ''')
    except Exception as e:
        logging.getLogger().error("An exception occurred while creating table", repr(e))

    try:
        logging.getLogger().info("Starting to fill DB with data from API, hitting API end point")
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        users = response.json()  # Parse JSON data

        for user in users:
            cursor.execute('''
            INSERT OR REPLACE INTO users (userId, id, title, completed)
            VALUES (?, ?, ?, ?)
            ''', (user['userId'], user['id'], user['title'], user['completed']))
    except Exception as e:
        logging.getLogger().error("An exception occurred while filling table with data from API", repr(e))

    commit_and_close_connection(cursor, conn)
    logging.info("Database and 'users' table created successfully.")


def query_db(query, params=None, fetchall=False):
    (cursor, conn) = create_connection()
    result = None
    try:
        # Execute the query with parameters if provided
        if params is not None:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if fetchall:
            result = cursor.fetchall()  # Fetch all rows if fetchall is True
        else:
            result = cursor.fetchone()  # Fetch a single row
    except Exception as e:
        logging.getLogger().error("An exception occurred while executing query {} against DB".format(query), repr(e))

    commit_and_close_connection(cursor, conn)
    return result
