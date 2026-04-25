import sqlite3
from book_des_db import BookDescriptionDB


def show_descriptions(limit=10):

    conn = sqlite3.connect("book_des.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT mds_code, bookid, title, description
        FROM book_description
        LIMIT ?
    """,
        (limit,),
    )

    rows = cursor.fetchall()

    for mds_code, bookid, title, description in rows:

        print("MDS:", mds_code)
        print("BookID:", bookid)
        print("Title:", title)

        desc = description or ""

        print("Description:", desc[:200], "...")

        print("-" * 60)

    conn.close()


if __name__ == "__main__":

    show_descriptions()
    # db = BookDescriptionDB()
    # db.delete_by_bookid("622651")
    # print(db.search_by_bookid("622651"))
