import sqlite3
import time
import random

from browser_driver import BrowserDriver
from work_crawler import LibraryThingWorkCrawler
from book_des_db import BookDescriptionDB


def get_unprocessed_books():

    conn1 = sqlite3.connect("book_id.db")
    conn2 = sqlite3.connect("book_des.db")

    cur1 = conn1.cursor()
    cur2 = conn2.cursor()

    cur1.execute(
        """
        SELECT mds_code, bookid, title
        FROM book_id
    """
    )

    all_books = cur1.fetchall()

    cur2.execute(
        """
        SELECT mds_code, bookid
        FROM book_description
    """
    )

    crawled = set(cur2.fetchall())

    conn1.close()
    conn2.close()

    remaining = [book for book in all_books if (book[0], book[1]) not in crawled]

    return remaining


def main():

    driver = BrowserDriver()
    crawler = LibraryThingWorkCrawler()
    db = BookDescriptionDB()

    books = get_unprocessed_books()

    print("Remaining books:", len(books))

    # first visit the hoomepage to select the language, in order to avoid being blocked by the website
    driver.get_page("https://www.librarything.com/")
    time.sleep(15)

    for mds_code, bookid, title in books:

        url = f"https://www.librarything.com/work/{bookid}/"

        print("Crawling:", url)

        driver.get_page(url)

        time.sleep(random.uniform(3, 5))

        html = driver.current_page()

        description = crawler.parse_description(html)
        print("Parsed description:", description)

        db.insert_book(mds_code, bookid, title, description)

        print("Saved:", title)

    driver.close()
    db.close()


if __name__ == "__main__":
    main()
