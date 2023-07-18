import os
import pathlib as pl
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import h5py
from tqdm import tqdm

for dirname, _, filenames in os.walk('/kaggle/'):
    for filename in filenames:
        if "hdf5" in filename: 
            print(filename, " shape:")
            with h5py.File(os.path.join(dirname,filename), 'r') as h5f:
                print(h5f['input'].shape)
                print(h5f['labels'].shape)

def tsv_to_hdf5(tsv_path, hdf5_path, percentage=1.0):
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

tsv_path = "/kaggle/input/c4200m/C4_200M.tsv-00000-of-00010"
hdf5_path = "/kaggle/working/C4_200M.hdf5-00000-of-00010"
percentage = 0.1  # 1% of the source data

tsv_to_hdf5(tsv_path, hdf5_path, percentage)