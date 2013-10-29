import sqlite3
import sys
import random

DB = None
CONN = None
#sqlite> CREATE TABLE Jokes (id integer primary key autoincrement, question varchar(140), answer varchar(140));


def init_db():
	# opening, reading, and closing file
	_f = open("jokes.txt")
	input_text = _f.readline()
	while(input_text):
		q_and_a = input_text.split('--')
		make_joke(q_and_a[0], q_and_a[1])
		input_text = _f.readline()
	_f.close()
	
def count_jokes():
    connect_to_db()
    query = """SELECT max(id) from jokes"""
    DB.execute(query,())
    row = DB.fetchone()
    CONN.close()
    if row:
        return row[0]
    else:
        return None

def get_joke_by_id(joke_id):
    connect_to_db()
    query = """SELECT question, answer from jokes where id = ?"""
    
    DB.execute(query, (joke_id,))
    row = DB.fetchone()
    CONN.close()
    if row:
        return row[0], row[1]
    else:
        return None

def make_joke(question, answer):
    connect_to_db()
    query = """INSERT into jokes (question, answer) values(?, ?)"""
    DB.execute(query, (question, answer))
    CONN.commit()
    CONN.close()

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("jokes.db")
    DB = CONN.cursor()


def main():	
    connect_to_db()
    CONN.close()

if __name__ == "__main__":
    main()
