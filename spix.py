from threading import RLock
from tracker import Tracker


class SPIX:
    rows = ['url']
    input_address = 'data.txt'
    input_content = None
    input_type = 'txt'

    output_address = 'result'
    output_type = 'txt'

    locker = RLock()
    threads = []

    @classmethod
    def get_input(cls):

        if SPIX.input_type not in ['txt']:
            raise ValueError("The extension " + SPIX.input_type + " is not supported for now")

        try:
            with open(SPIX.input_address, 'r') as f:
                SPIX.input_content = f.read().strip().split("\n")

        except FileNotFoundError:
            print("The input file does not exist")
            exit(1)

    @classmethod
    def run(cls):
        Tracker.rows = SPIX.rows

        try:

            for index, row in enumerate(SPIX.input_content):
                row = row.split(' ')
                if len(row) != len(SPIX.rows):
                    raise ValueError("The file is not malformed, the lines has different number of columns")

                tracker = Tracker(locker=SPIX.locker, data=row)
                tracker.start()

                SPIX.threads.append(tracker)

        except TypeError:
            print("An error occurred: looping a NoneType variable")
            exit(1)

    @classmethod
    def dump_output(cls):

        filename = SPIX.output_address + "." + SPIX.output_type

        data = ""
        for r in Tracker.broken_urls:
            result = ""
            for key in SPIX.rows:
                result += " %s" % r[key]

            data += result.lstrip() + "\n"

        rows = ' '.join(SPIX.rows)

        try:
            with open(filename, 'w') as f:
                f.write(rows + "\n")
                f.write(data)

        except FileNotFoundError:
            print("The output file does not exist")
            exit(1)


if __name__ == "__main__":

    SPIX.rows.append("table")
    SPIX.rows.append("id")

    SPIX.input_type = 'txt'
    SPIX.input_address = 'test.txt'

    SPIX.get_input()
    SPIX.run()

    for t in SPIX.threads:
        t.join()

    SPIX.dump_output()
