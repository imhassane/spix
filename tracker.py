from threading import Thread
import requests


class Tracker(Thread):
    rows = []
    broken_urls = []

    def __init__(self, locker, data):
        Thread.__init__(self)

        self.locker = locker
        self.data = data

    @classmethod
    def is_url_broken(cls, url):
        try:
            requests.get(url)
            return False
        except requests.exceptions.ConnectionError:
            return True

    def run(self):

        if len(Tracker.rows) > 0:

            is_broken = Tracker.is_url_broken(self.data[0])

            if is_broken:
                with self.locker:
                    data = {}

                    for index, key in enumerate(Tracker.rows):
                        data[key] = self.data[index]

                    Tracker.broken_urls.append(data)
