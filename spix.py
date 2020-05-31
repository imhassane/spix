from threading import RLock
from tracker import Tracker


class SPIX:
    rows = ['url']
    input_address = None
    input_content = None
    input_type = 'txt'

    output_address = 'result'
    output_type = 'txt'

    locker = RLock()
    threads = []

    @classmethod
    def get_input(cls, ext='txt', address='data'):

        if ext == 'txt':
            SPIX.input_type = 'txt'

        else:
            raise ValueError("The extension " + ext + " is not supported for now")

        SPIX.input_address = address

        with open(address, 'r') as f:
            SPIX.input_content = f.read().split("\n")

    @classmethod
    def run(cls):
        Tracker.rows = SPIX.rows

        for index, row in enumerate(SPIX.input_content):
            row = row.split(' ')
            if len(row) != len(SPIX.rows):
                raise ValueError("The file is not malformed, the lines has different number of columns")

            tracker = Tracker(locker=SPIX.locker, data=row)
            tracker.start()

            SPIX.threads.append(tracker)

    @classmethod
    def dump_output(cls):

        filename = SPIX.output_address + "." + SPIX.output_type

        data = ""
        for r in Tracker.broken_urls:
            result = ""
            for key in SPIX.rows:
                result += " %s" % r[key]

            data += result.lstrip() + "\n"

        with open(filename, 'w') as f:
            f.write(data)


if __name__ == "__main__":
    SPIX.get_input(ext='txt', address='test.txt')
    SPIX.run()

    for t in SPIX.threads:
        t.join()

    SPIX.dump_output()
