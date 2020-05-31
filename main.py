from argparse import ArgumentParser

from spix import SPIX
from tracker import Tracker


def main():
    parser = ArgumentParser()
    parser.add_argument("--rows", help="The rows of your input file")
    parser.add_argument("--input-type", help="The extension of your input file, supported are: txt")
    parser.add_argument("--input-address", help="The address of your input file")
    parser.add_argument("--output-type", help="The extension of your output file, supported are: txt")
    parser.add_argument("--output-address", help="The address of your output file without the extension")

    args = parser.parse_args()

    if args.input_type:
        SPIX.input_type = args.input_type

    if args.input_address:
        SPIX.input_address = args.input_address

    if args.rows:
        SPIX.rows.extend(args.rows.strip().split(' '))

    if args.output_type:
        SPIX.output_type = args.output_type

    if args.output_address:
        SPIX.output_address = args.output_address

    print("SPIX Broken url finder")

    print("STEP 1/3: Getting the file content")
    SPIX.get_input()

    print("STEP 2/3: Filtering broken urls")
    SPIX.run()

    print("\t waiting for threads to end...")
    for t in SPIX.threads:
        t.join()

    print("STEP 3/3: Dumping results into the output file: " + SPIX.output_address)
    SPIX.dump_output()

    print(len(Tracker.broken_urls), "brokens url found")
    print("Done. Check your output file to see the broken urls and eventually replace them")
    print("😍😍")


main()
