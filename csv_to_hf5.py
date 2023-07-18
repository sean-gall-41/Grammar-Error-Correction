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
    parser.add_argument('tsv_path', help='Path to the TSV file')
    parser.add_argument('hdf5_path', help='Path to save the resulting HDF5 file')
    parser.add_argument('--percentage', type=float, default=1.0, help='Percentage of lines to convert (default: 1.0)')
    args = parser.parse_args()

    convert_tsv_to_hdf5(args.tsv_path, args.hdf5_path, args.percentage)

if __name__ == '__main__':
    main()