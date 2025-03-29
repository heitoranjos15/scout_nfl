import requests
from bs4 import BeautifulSoup


def __get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"
    }

    response = requests.get(url, headers=headers)
    print(url)
    print(response.status_code)
    return response.text


def __parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_soup(url):
    return __parse_html(__get_html(url))


team_keys = {
    "arizona-cardinals": "crd",
    "atlanta-falcons": "atl",
    "baltimore-ravens": "rav",
    "buffalo-bills": "buf",
    "carolina-panthers": "car",
    "chicago-bears": "chi",
    "cincinnati-bengals": "cin",
    "cleveland-browns": "cle",
    "dallas-cowboys": "dal",
    "denver-broncos": "den",
    "detroit-lions": "det",
    "green-bay-packers": "gnb",
    "houston-texans": "htx",
    "indianapolis-colts": "clt",
    "jacksonville-jaguars": "jax",
    "kansas-city-chiefs": "kan",
    "las-vegas-raiders": "rai",
    "los-angeles-chargers": "sdg",
    "los-angeles-rams": "ram",
    "miami-dolphins": "mia",
    "minnesota-vikings": "min",
    "new-england-patriots": "nwe",
    "new-orleans-saints": "nor",
    "new-york-giants": "nyg",
    "new-york-jets": "nyj",
    "philadelphia-eagles": "phi",
    "pittsburgh-steelers": "pit",
    "san-francisco-49ers": "sfo",
    "seattle-seahawks": "sea",
    "tampa-bay-buccaneers": "tam",
    "tennessee-titans": "oti",
    "washington-football-team": "was"
}
