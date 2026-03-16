import sqlite3


def count_books_by_mds(db_name="book_id.db"):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    query = """
    SELECT mds_code, COUNT(*) 
    FROM book_id
    GROUP BY mds_code
    ORDER BY mds_code
    """

    cursor.execute(query)

    results = cursor.fetchall()

    for mds_code, count in results:
        print(f"MDS {mds_code}: {count} books")

    conn.close()


if __name__ == "__main__":
    count_books_by_mds()
