
import argparse

from rq import Queue

from timer import timed
from work import do_slow_piece_of_work
from worker import conn

q = Queue(connection=conn)


def do_the_thing_synchronously():
    do_slow_piece_of_work()

def do_the_thing_asynchronously():
    q.enqueue(do_slow_piece_of_work)

@timed
def do_the_thing(should_do_async):
    if should_do_async:
        do_the_thing_asynchronously()
    else:
        do_the_thing_synchronously()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--do_async', required=True, choices=['true', 'false'])

    args = parser.parse_args()

    do_async = {'true': True, 'false': False}[args.do_async]

    do_the_thing(do_async)
