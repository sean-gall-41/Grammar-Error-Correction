# GEC with Transformer

This is a project as part of NeuroMatch Academy 2023 which aims to evaluate Grammar Error Correction
and Detection on transformers.

---

## Instructions:


### Data conversion

Use this  [kaggle notebook](https://www.kaggle.com/code/dariocioni/c4-200m-usage) to get the data, click on Copy my edit to get you a new notebook. Use the [util file to convert tsv to hdf5](./csv_to_hf5.py).

you can run your script from the command line like this:
```bash
python csv_to_hf5.py tsv_path hdf5_path --percentage 0.1
```

### Run the model

By using [baseline notebook](./gec-with-transformers-from-scratch.ipynb) you can run the model.





---

### Credits

Original code is presented [here](https://www.kaggle.com/datasets/dariocioni/c4200m).