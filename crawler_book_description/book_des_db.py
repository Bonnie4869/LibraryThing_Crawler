import sqlite3


class BookDescriptionDB:

    def __init__(self, db_name="book_des.db"):

        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS book_description (
            mds_code TEXT,
            bookid TEXT,
            title TEXT,
            description TEXT,
            PRIMARY KEY (mds_code, bookid)
        )
        """

        self.conn.execute(query)

        self.conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_bookid ON book_description(bookid)"
        )

        self.conn.commit()

    def insert_book(self, mds_code, bookid, title, description):

        query = """
        INSERT OR IGNORE INTO book_description
        (mds_code, bookid, title, description)
        VALUES (?, ?, ?, ?)
        """

        self.conn.execute(query, (mds_code, bookid, title, description))

        self.conn.commit()

    def close(self):

        self.conn.close()
