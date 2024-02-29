""" ex_5_2.py
This module contains an entry point that

- loads data from a file `ex_5_2-data.csv` into a numpy array
- shifts and scales the data such that the resulting mean
        is 0 and the standard deviation is 1.
- writes the processed data to a file called `ex_5_2-processed.csv`
"""
import numpy as np
import csv

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root


if __name__ == "__main__":

    # Use these predefined input / output files
    root_dir = get_repository_root()
    INFILE = root_dir / "data" / "ex_5_2-data.csv"
    OUTFILE = root_dir / "outputs" / "ex_5_2-processed.csv"

    # Complete the data processing steps using numpy here.
    with open(INFILE,'r') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)
        numpy_array = np.array(data, dtype=float)
        new_array = numpy_array - np.mean(numpy_array)

        std_dev = np.std(new_array)
        processed = new_array/std_dev

    # Save the output to OUTFILE using numpy routines.
        np.savetxt(OUTFILE, processed)
