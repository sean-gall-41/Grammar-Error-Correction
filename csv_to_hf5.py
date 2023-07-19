#!/usr/bin/env python

import os
import argparse
import pathlib as pl
import pandas as pd
import h5py
from tqdm import tqdm

def convert_tsv_to_hdf5(tsv_path, hdf5_path, percentage=1.0):
    df = pd.read_csv(tsv_path, sep='\t', header=None, names=['input', 'labels'])
    num_lines = int(len(df) * percentage)

    hdf_filename = pl.Path(hdf5_path)
    dt = h5py.special_dtype(vlen=str)

    with h5py.File(hdf_filename, 'w') as h5f:
        dset1 = h5f.create_dataset('input', shape=(num_lines,), dtype=dt, chunks=True)
        dset2 = h5f.create_dataset('labels', shape=(num_lines,), dtype=dt, chunks=True)

        with tqdm(total=num_lines, desc="Converting", unit="line") as pbar:
            for i, (input_value, label_value) in df.iterrows():
                dset1[i] = str(input_value)
                dset2[i] = str(label_value)
                pbar.update(1)
                if i + 1 >= num_lines:
                    break

def main():
    parser = argparse.ArgumentParser(description='Convert TSV file to HDF5 format.')
    parser.add_argument('--percentage', type=float, nargs='?', default=1.0, help='Percentage of lines to convert (default: 1.0)')
    subparsers = parser.add_subparsers(help='possible subcommands', dest="subcommand")
    
    # create the parser for the "single" command
    parser_single = subparsers.add_parser('single', help='convert a single TSV file to HDF5 format')
    parser_single.add_argument('-i', '--input', type=str, help='Path to the TSV file')
    parser_single.add_argument('-o', '--output', type=str, help='Path to save the resulting HDF5 file')

    # create the parser for the "command_2" command
    parser_batch = subparsers.add_parser('batch', help='convert a batch of TSV files to HDF5 format')
    parser_batch.add_argument('-i', '--input', type=str, help='Path to a set of TSV files to be processed')

    args = parser.parse_args()

    match args.subcommand:
        case 'single':
            if args.input is not None and args.output is not None:
                print(f"Converting '{args.input}' -> '{args.output}'")
                convert_tsv_to_hdf5(args.input, args.output, args.percentage)
            else:
                parser.error("One or either of positional arguments missing for subcommand 'single'.")
        case 'batch':
            if args.input is not None:
                file_list = os.listdir(args.input)
                tsv_files = [filename for filename in file_list if 'tsv' in filename and 'zip' not in filename]
                for tsv_filename in tsv_files:
                    full_tsv_path = f"{args.input}{tsv_filename}"
                    full_hdf5_path = f"{args.input}{tsv_filename.replace('tsv', 'hdf5')}"
                    print(f"Converting '{full_tsv_path}' -> '{full_hdf5_path}'")
                    convert_tsv_to_hdf5(full_tsv_path, full_hdf5_path, args.percentage)
        case other:
            parser.error('You must include a subcommand!')

if __name__ == '__main__':
    main()

