from bs4 import BeautifulSoup


class LibraryThingWorkCrawler:

    from bs4 import BeautifulSoup


class LibraryThingWorkCrawler:

    def parse_description(self, html):

        soup = BeautifulSoup(html, "html.parser")

        # Cloudflare detection
        if "Enable JavaScript" in html:
            return "Net_blocked"

        # Check for title, if not found return Net_blocked
        title = soup.select_one("h1.h1_work_title")
        if not title:
            return "Net_blocked"

        desc = "None"
        try:
            desc = soup.select_one("#section_description span[id^='tdh_']")

        except Exception as e:
            print(f"Error occurred while parsing description: {e}")

        if not desc:
            return "None"

        text = desc.get_text(" ", strip=True)

        text = text.replace("show more", "")
        text = text.replace("show less", "")
        text = text.replace("顯示更多", "")
        text = text.replace("顯示更少", "")

        text = text.strip()

        if not text:
            return "None"

        return text
