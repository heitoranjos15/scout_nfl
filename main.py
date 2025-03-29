import os
import logging
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from src import news, team_data


async def send_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    content_list = news.run()

    for content in content_list:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'{content.get("title")}\n {content.get("link")}\n---------------------------'
        )


async def select_team(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "what team do you want to see the data?"
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )
    register_team_handler = CommandHandler("team_data", get_team_data)
    context.dispatcher.add_handler(register_team_handler)


async def get_team_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    team = update.message.text
    content = team_data.run_by_team(team)
    text = f'Coach: {content.get("info").get("coach")}\n'
    for game in content.get("games"):
        text += f'{game.get("date")} {game.get("hour")} {game.get("home_game")} {game.get("opponent")}\n'

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )


def test():
    print("new", news.run())
    print("team", team_data.run_by_team("buffalo-bills"))


def main():
    load_dotenv()
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    print(telegram_token)
    logging.basicConfig(level=logging.DEBUG)

    app = ApplicationBuilder().token(telegram_token).build()
    new_handler = CommandHandler("news", send_news)
    new_handler = CommandHandler("team_data", select_team)
    app.add_handler(new_handler)
    app.run_polling()


if __name__ == "__main__":
    # main()
    test()
