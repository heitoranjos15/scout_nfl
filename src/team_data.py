import os
import logging
from dotenv import load_dotenv
from src.utils import get_content, team_keys


def get_games(soup):
    contents = list()
    gamesList = soup.select("table#games > tbody > tr")
    for game in gamesList:
        colums = game.select("td")
        if len(colums) == 0:
            logging.info("No columns found")
            continue
        date = colums[1].text.strip()
        hour = colums[2].text.strip()
        game_type = colums[7].text.strip()
        home_game = game_type != "@"
        opponent = colums[8].text.strip()
        contents.append({
            "date": date,
            "hour": hour,
            "home_game": home_game,
            "opponent": opponent
        })

    return contents


def get_info(soup) -> dict:
    infoList = soup.select("div#meta > div:nth-of-type(2) > p")
    if len(infoList) == 0:
        logging.info("No info found")
        return {
            "coach": "",
            "off_cor": "",
            "def_cor": ""
        }

    coach = infoList[1].text.strip().replace("Coach:\n", "")
    off_cor = infoList[7].text.strip()
    def_cor = infoList[8].text.strip()
    return {
        "coach": coach,
        "off_cor": off_cor,
        "def_cor": def_cor
    }


def get_transactions(soup) -> list:
    content = list()
    transactionList = soup.select("div.stacktable > div.tr")
    if len(transactionList) == 0:
        logging.info("No transactions found")
        return content

    for transaction in transactionList:
        transaction_data = transaction.select("div")
        date = transaction_data[0].text.strip()
        description = transaction_data[1].text.strip()
        content.append({
            "date": date,
            "description": description
        })
    return content


def run_by_team(team, team_key=None) -> dict:
    scope = "nfl_team_data"
    FORMAT = f'%(asctime)-15s [{scope}] - {team} %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO)
    load_dotenv()

    if not team_key:
        team_key = team_keys.get(team)
        if not team_key:
            raise Exception("Team not found")

    url_profootball = os.getenv("URL_PROFOOTBALLREFERENCE")
    stats_team_url = f"{url_profootball}/teams/{team_key}/2024.htm"
    stats_content = get_content(stats_team_url)

    games = get_games(stats_content)
    info = get_info(stats_content)

    url_footballdb = os.getenv("URL_FOOTBALLDB")
    transactions_url = f"{url_footballdb}/teams/nfl/{team}/transactions"
    transactions_content = get_content(transactions_url)
    transactions = get_transactions(transactions_content)

    return {
        "games": games,
        "info": info,
        "transactions": transactions
    }
