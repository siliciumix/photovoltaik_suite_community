from logfile_api import *
from datetime import timedelta
from config_api import *
from logfile_api import *
import os

def print_dates(conf):
    start_date = logfile.start_datum()
    today_date = logfile.heute_datum()
    yesterday_date = logfile.gestern_datum()
    days = logfile.div_days(today_date, start_date)
    ifadress = conf["speicher"]["ip"]

    print(f"Startdatum     : {start_date}")
    print(f"Heutiges Datum : {today_date}")
    print(f"Gestriges Datum: {yesterday_date}")
    print(f"Tage           : {days}")
    print(f"Speicher IP    : {ifadress}")
    print()


def logfile_laden():
    conf = config.read(os.getenv("CONFIG_FILE"))
    print_dates(conf)

    if conf["logfile"]["cronjob"]:
        if conf["logfile"]["yester"]:
            start_date = logfile.gestern_datum()
        else:
            start_date = logfile.heute_datum()
        max_day = logfile.div_days(start_date, start_date)
    else:
        start_date = logfile.start_datum()
        max_day = logfile.div_days(logfile.heute_datum(), start_date)

    for tag_counter in range(max_day):
        datum = start_date + timedelta(tag_counter)
        logfile.save_logfile(datum)


if __name__ == "__main__":
    logfile_laden()
