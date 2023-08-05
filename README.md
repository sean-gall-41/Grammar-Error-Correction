# GEC

This repository contains code for the NeuroMatch Academy (NMA 2023) DL summer course project attempting to evaluate Grammar Error Correction and Detection with neural networks.

The project is mainly an exercise to replicate findings from different NNs for GEC by re-implementing and evaluating several basic analyses.

---

## Instructions:


### Data conversion

Use this  [kaggle notebook](https://www.kaggle.com/code/dariocioni/c4-200m-usage) to get the data, click on Copy my edit to get you a new notebook. Use the [util file to convert tsv to hdf5](./csv_to_hf5.py).

There are two modes which are available as subcommands. The first is 'single file' mode, which converts one specified tsv file to hdf5
Its usage is as the following:

```bash
python csv_to_hf5.py single [-h] [-i TSV_PATH] [-o HDF5_PATH] [--percentage 0.1 (default 0.1)]
```
The next mode is 'batch' mode. Here you specify the folder containing a set of input tsv files and they are automatically converted and given the same name, just
with *tsv* changed to *hdf5*. Its usage is as the following:

```bash
python csv_to_hf5.py batch [-h] [-i INPUT_DIR] [--percentage 0.1 (default 0.1)]
```

### Run the model

By using [baseline notebook](./gec-with-transformers-from-scratch.ipynb) you can run the model.



---

### Credits

Original code is presented [here](https://www.kaggle.com/datasets/dariocioni/c4200m).
