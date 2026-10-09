import os
import numpy as np
import pandas as pd

from src.data_loader import get_project_root 

def load_features_weights_matrix():

    features_weights_dir_path = os.path.join(get_project_root(), "data", "features_weights")
    arr_final_path = os.path.join(features_weights_dir_path, "numpy_features_weights_arr.npy")
    features_weights = np.load(arr_final_path)

    # Check if every feature have at least one non zero weight. Conversely, we can delete that feateure because it has no importance
    rows_used_features_idx, columns_used_features_idx = np.where(features_weights !=0)
    # The output is a tuple representing the indices of both rows and columns which meet teh !=0 condition.
    # Actually, the indices of the columns also represents the indices of the most important original dataset features
    
    best_features_indices = np.unique(columns_used_features_idx)

    reduced_features_weights = features_weights[:, best_features_indices]
    absolute_reduced_features_weights = np.absolute(reduced_features_weights)

    feature_per_class_absolute_max_weight = np.max(absolute_reduced_features_weights, axis=0)
    absolute_max = np.max(feature_per_class_absolute_max_weight)
    absolute_min = np.min(feature_per_class_absolute_max_weight)

    return [
        features_weights, best_features_indices, 
        feature_per_class_absolute_max_weight, 
        absolute_max, absolute_min
    ]

def create_reduced_dataset(X, threshold=None):

    # Load the necessary objects using the above function. Thanks to it the user can define a 
    features_weights, best_features_indices, feature_per_class_absolute_max_weight, absolute_max, absolute_min = load_features_weights_matrix()

    # This block of code below yields an array containing the indices values for the columns of the original features_weights 2d array
    # which meet the desidered condition specified using the "treshold" parameter. If no "treshold" parameter is given then the default
    # condition is used: (absolute_max - absolute_min) / 2

    if threshold is None:
        threshold = ((absolute_max - absolute_min) / 2)
        best_reduced_features_idx = np.where(feature_per_class_absolute_max_weight > threshold)[0]
    else:
        best_reduced_features_idx = np.where(feature_per_class_absolute_max_weight > threshold)[0]

    final_original_features_idx = best_features_indices[best_reduced_features_idx]
    final_weights = features_weights[:, final_original_features_idx]

    # Process the original data.
    # Assumes that X is a 2D array or a Pandas DataFrame
    if isinstance(X, np.ndarray):
        X_reduced = X[:, final_original_features_idx]
    else:
        X_reduced = X.iloc[:, final_original_features_idx]

    return X_reduced