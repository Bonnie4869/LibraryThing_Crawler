import sqlite3


class BookIDDB:

    def __init__(self, db_name="book_id.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS book_id (
            mds_code TEXT,
            bookid TEXT,
            title TEXT,
            PRIMARY KEY (bookid, mds_code)
        )
        """

        self.conn.execute(query)
        self.conn.commit()

    def insert_book(self, mds_code, bookid, title):

        query = """
        INSERT OR IGNORE INTO book_id (mds_code, bookid, title)
        VALUES (?, ?, ?)
        """

        self.conn.execute(query, (mds_code, bookid, title))
        self.conn.commit()

    def close(self):
        self.conn.close()
