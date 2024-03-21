import datetime

#milliseconds to date time.
def ms_to_dt(ms: int):
    return datetime.datetime.utcfromtimestamp(ms / 1000)