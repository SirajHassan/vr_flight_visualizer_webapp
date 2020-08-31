from redis import Redis
from rq import Queue
from .update_request_data import update_request_data


def test(pk):
    q = Queue(connection=Redis())
    update_request_data(pk)
    # result = q.enqueue(update_request_data,3)
    print("added to queue")
