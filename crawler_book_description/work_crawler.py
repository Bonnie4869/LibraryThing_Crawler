from bs4 import BeautifulSoup


class LibraryThingWorkCrawler:

    from bs4 import BeautifulSoup


class LibraryThingWorkCrawler:

    def parse_description(self, html):

        soup = BeautifulSoup(html, "html.parser")

        # Cloudflare detection
        if "Enable JavaScript" in html:
            return "Net_blocked"

        desc = soup.select_one("#section_description span[id^='tdh_']")

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
