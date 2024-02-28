import sqlite3
import argparse, textwrap

def add_table(cur: sqlite3.Cursor, table_name: str):
    """
        Adds a table to the database.

        Checks if table already exists in database. If it does, then
        it prints a message and SKIPS table creation.
    """
    res = cur.execute(
        f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'; "
        ).fetchall()
    print(f"res: {res}")
    
    if res is []:
        cur.execute("CREATE TABLE movies(title, year)")
        print(f"Table created: {table_name}")
    else:
        print(f"Error in add_table: Table already exists.")

def drop_table(conn: sqlite3.Connection, table_name: str):
    """Drops table from database. USE CAREFULLY."""
    conn.execute(f"DROP TABLE {table_name}")
    print(f"Table: {table_name} ...dropped")

def main():
    print("Welcome to pytlitedb...")

    parser = argparse.ArgumentParser(
        prog='pylite',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
                            Examples:
                                pylite.py --options [go here]
                        '''))
    parser.add_argument('--action', type=str, required=False, dest='arg_action', help="An action to execute.")

    con = sqlite3.connect('sample.db')
    cur = con.cursor()

    # add_table(cur, 'movies')
    drop_table(con, 'movie')
    
    res = cur.execute("SELECT name FROM sqlite_master")
    data = res.fetchone()

    print(f"data: {data}")

if __name__ == "__main__":
    main();