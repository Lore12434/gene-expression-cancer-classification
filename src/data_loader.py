import os
import pandas as pd
import sklearn
import numpy as np

def get_project_root():

    current_dir = os.getcwd()
    # Get the layer above (project folder)
    if os.path.basename(current_dir) in ["notebooks", "src"]:
        return os.path.dirname(current_dir)

    return current_dir


def load_and_save_data(test_size=0.3):

    project_dir = get_project_root()
    data_path = os.path.join(project_dir, "data")
    raw_path = os.path.join(data_path, "raw")
    
    if not os.path.exists(raw_path):
        print(f"Directory not found at: {raw_path}")
        return None


    x_path = os.path.join(raw_path, "data.csv")
    y_path = os.path.join(raw_path, "labels.csv")
    genes_path = os.path.join(raw_path, "unc.edu_PANCAN_IlluminaHiSeq_RNASeqV2.geneExp.tsv")


    if not os.path.isfile(genes_path):
        print(f"'unc.edu_PANCAN_IlluminaHiSeq_RNASeqV2.geneExp.tsv' which contains the original genes names not found at: {genes_path}")
    else:
        genes_df = pd.read_csv(genes_path, sep="\t", encoding="utf-8", usecols=[0])
        genes_names = genes_df.iloc[:, 0].to_list()
    
    if not os.path.isfile(x_path):
        print(f"'data.csv' not found at: {x_path}")
        return None
    else:
        X = pd.read_csv(x_path, index_col=0)
        X_col = X.columns
        dict = {old_name: gene_name for old_name, gene_name in zip(X_col, genes_names)}
        X_formatted = X.rename(columns=dict)

    if not os.path.isfile(y_path):
        print(f"'labels.csv' not found at: {y_path}")
        return None
    else:
        y = pd.read_csv(y_path, index_col=0)
        y = y["Class"]


    processed_path = os.path.join(data_path, "processed")
    os.makedirs(processed_path, exist_ok=True)
        
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
        X_formatted, y, test_size=test_size, random_state=42
    )

    names = ["X_train.csv", "X_test.csv", "y_train.csv", "y_test.csv"]
    all_datasets = [X_train, X_test, y_train, y_test]
    
    for name, dataset in zip(names, all_datasets):
        save_file_path = os.path.join(processed_path, name)
        print(f"Saving {name}...")
        dataset.to_csv(save_file_path)
        
    print("All datasets are been successfully saved to data/processed!")
    return None

from pathlib import Path
import pandas as pd


def import_data():

    project_dir = get_project_root()
    processed_dir = os.path.join(project_dir, "data", "processed")

    if not os.path.exists(processed_dir):
        raise FileNotFoundError(
            f"Processed data directory not found at: {processed_dir}. "
            "Make sure to run load_and_save_data() first!"
        )


    # 1. Load Features
    X_train = pd.read_csv(
        os.path.join(processed_dir, "X_train.csv"), 
                     index_col=0)
    X_test = pd.read_csv(
        os.path.join(processed_dir, "X_test.csv"), 
        index_col=0)

    # 2. Load Labels (flattened)
    y_train = pd.read_csv(
        os.path.join(processed_dir, "y_train.csv"), 
        index_col=0).squeeze()
    
    y_test = pd.read_csv(
        os.path.join(processed_dir, "y_test.csv"), 
                     index_col=0).squeeze()

    return X_train, X_test, y_train, y_test