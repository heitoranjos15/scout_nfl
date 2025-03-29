import logging


def get_transactions(soup) -> list:
    transaction_content = list()
    transactionList = soup.select("div.stacktable > div.tr")
    if len(transactionList) == 0:
        logging.info("No transactions found")
        return transaction_content

    for transaction in transactionList:
        transaction_data = transaction.select("div")
        date = transaction_data[0].text.strip()
        description = transaction_data[1].text.strip()
        transaction_content.append({
            "date": date,
            "description": description
        })
    return transaction_content
