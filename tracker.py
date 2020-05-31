from threading import Thread


class Tracker(Thread):

    rows = []
    broken_urls = []

    def __init__(self, locker, data):
        Thread.__init__(self)

        self.locker = locker
        self.data = data

    def run(self):

        with self.locker:
            Tracker.broken_urls.append({"url": self.data[0]})
