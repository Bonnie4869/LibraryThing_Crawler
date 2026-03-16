# in book_id crawler, you only need to set the variables below, without changing other pieces of the code
# input the DDC codes you want to crawl
DDC = [
    "104",
    "105",
    "107",
    "108",
    "112",
    "118",
    "119",
    "120",
    "125",
    "127",
    "134",
    "136",
    "137",
    "138",
    "139",
    "145",
    "151",
    "161",
    "162",
    "163",
    "164",
    "166",
    "169",
]

# set the maximum number of pages to crawl for each DDC code (each page has 50 books)
MAX_CRAWL_PAGE_NUM = 3  # 50 books per page
