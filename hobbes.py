from requests import get
from bs4 import BeautifulSoup

BASE_URL = "https://www.gocomics.com"
FIRST_COMIC = "/calvinandhobbes/1985/11/18"

class Comic:
    def __init__(self, image, date, next_comic):
        self.comic_image = image
        self.date = date
        self.next_comic = next_comic

    def save():
        """Saves the comic to disk in the current folder"""
        filename = "-".join(date.split("/")[2:])

        print("Downloading {0}".format(filename))

        with open("{}.gif".format(filename), "wb") as f:
            f.write(image)

def get_comic(date):
    """Retrives comic for the given date."""
    res = get(BASE_URL + date)
    soup = BeautifulSoup(res.content, "html.parser")

    image_url = soup.find("div", class_="comic")['data-image']
    image = get(image_url).content

    next_comic = soup.select("div.gc-calendar-nav__next > a.fa-caret-right")[0]['href']

    return Comic(image, date, next_comic)

comic = get_comic(FIRST_COMIC)
while comic.next_comic:
    comic = get_comic(comic.next_comic)

