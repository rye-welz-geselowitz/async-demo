from time import sleep

from timer import timed

SLEEP_SECONDS = 30

def do_slow_piece_of_work():
    _do_slow_piece_of_work()

@timed
def _do_slow_piece_of_work():
    sleep(SLEEP_SECONDS)