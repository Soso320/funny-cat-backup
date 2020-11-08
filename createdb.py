# This script creates a database intended to be used with the main bot for the tagging command
import sqlite3
from sqlite3 import Error
# if you decide to change the file name you will have to update the code accordingly
connection = sqlite3.connect("tagbot.sqlite")

with connection:
    connection.execute("""
        CREATE TABLE TAG (
            id INTEGER,
            name TEXT not null,
            content TEXT not null,
            date INTEGER,
            unique (name)
        );
    """)
