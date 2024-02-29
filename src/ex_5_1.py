"""ex_5_1.py"""
import argparse
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count


def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename argument from the command line
    # pass this argument to the main function above
    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (seeas README.md for more details)
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='This program prints the number of lines in infile.')
    args = parser.parse_args()
    filename_argument = args.infile
    main(filename_argument)
