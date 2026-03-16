from browser_driver import BrowserDriver
from page_crawler import LibraryThingCrawler
from selenium.webdriver.common.by import By
import time
from book_id_db import BookIDDB

browser_driver = BrowserDriver()
crawler = LibraryThingCrawler()
db = BookIDDB()
from config import DDC, MAX_CRAWL_PAGE_NUM


def main():

    # first visit the main page to avoid being blocked
    browser_driver.get_page("https://www.librarything.com/")
    time.sleep(10)

    codes = DDC
    base_url = "https://www.librarything.com/mds/{}"

    for code in codes:
        url = base_url.format(code)

        print("Crawling:", url)
        browser_driver.get_page(url)
        crawl_per_mds(code)

    browser_driver.close()
    db.close()


def crawl_per_mds(code, max_page_num=MAX_CRAWL_PAGE_NUM):

    # deal with page turning
    for i in range(max_page_num):
        print(f"Page {i+1}")
        time.sleep(5)
        html = browser_driver.driver.page_source

        books = crawler.parse_books(html)

        for book in books:

            db.insert_book(mds_code=code, bookid=book["bookid"], title=book["title"])

            print(code, book["title"], book["bookid"])

        # click "next" button
        try:
            next_button = browser_driver.driver.find_element(
                By.CSS_SELECTOR, "div.lt_shelf_pagination i.fa-chevron-right"
            ).find_element(By.XPATH, "..")

            # highlight the next button for debugging
            browser_driver.driver.execute_script(
                "arguments[0].style.outline='3px solid red';", next_button
            )
            time.sleep(0.5)

            next_button.click()

        except Exception:
            print("Last page reached")


if __name__ == "__main__":
    main()
