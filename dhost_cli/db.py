import sqlite3

from . import settings


def init_database():
    con = sqlite3.connect(settings.DATABASE_NAME)
    cur = con.cursor()

    # Check if table 'token' exist, create it if it does not
    table_token_count = cur.execute("""SELECT count(name)
        FROM sqlite_master
        WHERE type='table' AND name='token'""")
    table_exist = table_token_count.fetchone()[0] == 1
    if not table_exist:
        cur.execute("""CREATE TABLE token
            (access_token text, refresh_token text, expires text)
            """)

    con.commit()
    con.close()


def save_token(access_token, refresh_token='', expires=''):
    con = sqlite3.connect(settings.DATABASE_NAME)
    cur = con.cursor()
    cur.execute("INSERT INTO token VALUES ('{}', '{}', '{}')".format(
        access_token, refresh_token, expires))
    con.commit()
    con.close()
    return access_token


def fetch_all_tokens():
    token_list = None
    con = sqlite3.connect(settings.DATABASE_NAME)
    cur = con.cursor()
    token_list_query = cur.execute("SELECT * FROM token")
    token_list = token_list_query.fetchall()
    con.commit()
    con.close()
    return token_list


def fetch_token():
    tokens = (None, None, None)
    token_list = fetch_all_tokens()
    if len(token_list) >= 1:
        tokens = token_list[0]
    return tokens
