from requests import get
from bs4 import BeautifulSoup

BASE_URL = "https://www.gocomics.com"
FIRST_COMIC = "/calvinandhobbes/1985/11/18"

def get_comics_from(date):
    """Recursively retrives comics starting from the given date.

    Arguments:
    date -- the date of the comic to start with
    """
    res = get(BASE_URL + date)
    soup = BeautifulSoup(res.content, "html.parser")

    comic_image_url = soup.find("div", class_="comic")['data-image']
    formatted_date = "-".join(date.split("/")[2:])
    save_comic(comic_image_url, formatted_date)

    next_comic = soup.select("div.gc-calendar-nav__next > a.fa-caret-right")[0]['href']
    if next_comic is None:
        return
    else:
        get_comic(next_comic)

def save_comic(url, filename):
    """Saves the comic to disk in the current folder.
    The date of the comic is used as the filename.

    Arguments:
    url -- the url for the comic image
    filename -- filename used to save image
    """
    print("Downloading {0}".format(date))

    filename = "-".join(date.split("/")[2:])
    with open("{}.gif".format(filename), "wb") as f:
        resp = get(url)
        f.write(resp.content)

get_comics_from(FIRST_COMIC)
