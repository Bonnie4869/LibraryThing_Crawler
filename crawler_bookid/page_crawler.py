from bs4 import BeautifulSoup


class LibraryThingCrawler:

    def parse_books(self, html):

        soup = BeautifulSoup(html, "html.parser")

        books = []

        items = soup.select("div.shelforlist li")

        for item in items:

            title_tag = item.select_one("a[data-workid]")

            if not title_tag:
                continue

            title = title_tag.get_text(strip=True)
            bookid = title_tag.get("data-workid")

            books.append({"title": title, "bookid": bookid})

        return books
