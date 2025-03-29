import logging


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
