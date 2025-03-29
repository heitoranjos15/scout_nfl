# Betty

## Description
NFL scout to collect and store data from players and teams.
This project has integration with telegram bot and notion.

## Run
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Scouts
| scout | description |
| --- | --- |
| nfl_news | Collects news from NFL |
| nfl_teams | Collects general data from NFL teams |

## Telegram 
| command | description |
| --- | --- |
| /news | Get the latest news from NFL |
| /teams_data | Get general data from NFL teams |
