import logging


def get_games(soup):
    game_content = list()
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
        game_content.append({
            "date": date,
            "hour": hour,
            "home_game": home_game,
            "opponent": opponent
        })

    return game_content
