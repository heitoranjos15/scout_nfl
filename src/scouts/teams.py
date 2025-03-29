import os
import logging
from dotenv import load_dotenv
from src.utils import get_soup, team_keys
from src.scouts.team_data import games, info, transactions


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
    soup = get_soup(stats_team_url)

    game_content = games.get_games(soup)
    info_content = info.get_info(soup)

    url_footballdb = os.getenv("URL_FOOTBALLDB")
    transactions_url = f"{url_footballdb}/teams/nfl/{team}/transactions"
    soup = get_soup(transactions_url)
    transactions_content = transactions.get_transactions(soup)

    return {
        "games": game_content,
        "info": info_content,
        "transactions": transactions_content
    }
