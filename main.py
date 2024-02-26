import sqlite3

def main():
    print("Welcome to pytlitedb...")

    con = sqlite3.connect('sample.db')
    cur = con.cursor()

    # cur.execute("CREATE TABLE movie(title, year)")
    res = cur.execute("SELECT name FROM sqlite_master")
    data = res.fetchone()

    print(f"data: {data}")

if __name__ == "__main__":
    main();