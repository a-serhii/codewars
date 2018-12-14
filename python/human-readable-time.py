import datetime
import time


def make_readable(seconds):
    hours_need = (
        int(
            time.strftime(
                "%H", time.gmtime(datetime.timedelta(seconds=seconds).seconds)
            )
        )
        + datetime.timedelta(seconds=seconds).days * 24
    )
    min_sec = time.strftime(
        "%M:%S", time.gmtime(datetime.timedelta(seconds=seconds).seconds)
    )
    if len(str(hours_need)) == 1:
        ready = "0" + str(hours_need) + ":" + min_sec
    else:
        ready = str(hours_need) + ":" + min_sec
    return ready
