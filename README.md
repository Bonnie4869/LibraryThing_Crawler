# LibraryThing_Crawler
This project is a crawler to collect book description from LibraryThing website.


# 1. Description
This project is a crawler to collect book description from LibraryThing website.
You first need to crawl the book_id using `crawler_bookid` crawler, and get the book_id database.
Then, you can use `crawler_book_description` crawler to collect book description.

# 2. Usage
## 2.1 library
1. Install the dependencies in your environment.    
    ```pip install -r requirements.txt```

## 2.2 crawler_bookid
Run the crawler to collect book_id.
（1）Set the DDC codes you want to crawl in `config.py`.
（2）Set the `MAX_CRAWL_PAGE_NUM` in `config.py`, it is the max page num to crawl for each DDC code.
（3）Run the crawler.    
    ```python crawler_bookid/main.py```

## 2.3 crawler_book_description
Run the crawler to collect book description.
```python crawler_book_description/main.py```


# 3. Notice - MUST READ
1. When the crawler start running, it will wake up a browser and first visit the homepage of the website. You may be asked to `select language`, just select `English` or `繁体中文` or `do nothing` or `click the x to close the warning dialog`, do not select `others`.

2. When the crawler encounter the cloudflare detection:
(1) If it continue to go to the target page (page with detailed information of the book), just let it go, needn't to do anything.
(2) If you wait for a while, and the crawler show the cloudfare page all the time, please click anywhere on the page OR click the `tick` button on the page.
(3) if you meet the block by cloudfare, the `Net_blocked` will be shown in the console. (for description crawler)

# 4. File Structure
For crawler_bookid:
- main.py - Main orchestrator controlling the crawling flow
- browser_driver.py - Web browser automation with anti-detection
- page_crawler.py - HTML parsing using BeautifulSoup
- book_id_db.py - SQLite database management
- config.py - Configuration settings for DDC codes
- cnt_bookid_by_mds.py - Data analysis utility, you can use it to count the book_id by DDC code, just for debug and testing.

For crawler_book_description:
- crawl_description.py - Main description collection orchestrator
- browser_driver.py - Browser automation for description pages
- work_crawler.py - Description parsing with Cloudflare handling
- book_des_db.py - SQLite database management
- test.py - Data verification utility, you can use it to check the book description in the database, just for debug and testing.

