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

    def delete_by_bookid(self, bookid):
        query = "DELETE FROM book_description WHERE bookid = ?"
        self.conn.execute(query, (bookid,))
        self.conn.commit()

    def search_by_bookid(self, bookid):
        """根据 bookid 精确搜索"""
        query = "SELECT * FROM book_description WHERE bookid = ?"
        cursor = self.conn.execute(query, (str(bookid),))
        return cursor.fetchall()

    def count_net_blocked(self):
        query = """
        SELECT COUNT(*)
        FROM book_description
        WHERE description = 'Net_blocked'
        """
        cursor = self.conn.execute(query)
        return cursor.fetchone()[0]

    def delete_net_blocked(self):
        query = """
        DELETE FROM book_description
        WHERE description = 'Net_blocked'
        """
        cursor = self.conn.execute(query)
        self.conn.commit()
        return cursor.rowcount

    def close(self):

        self.conn.close()


db = BookDescriptionDB()
print(db.count_net_blocked())
print(db.delete_net_blocked())
db.close()
