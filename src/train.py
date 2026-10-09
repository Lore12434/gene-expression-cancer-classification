import os
import numpy as np
import pandas as pd
import joblib
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from src.data_loader import get_project_root, import_data
from src.preprocessing import create_reduced_dataset

def train():

    X_train, X_test, y_train, y_test = import_data()
    X_train_reduced = create_reduced_dataset(X_train)

    print("Initializing the Pipeline")
    final_pipeline = make_pipeline(
        StandardScaler(),
        LogisticRegression(random_state=42)
    )

    print("Training the Final Pipeline")
    final_pipeline.fit(X_train_reduced, y_train)

    models_dir = os.path.join(get_project_root(), "models")
    print("Saving the Final Pipeline")
    final_pipeline_path = os.path.join(models_dir, "final_pipeline_model")
    joblib.dump(final_pipeline, final_pipeline_path)
    print(f"Final Pipeline saved at: {final_pipeline_path}")

    return final_pipeline

if __name__ == "__main__":
    train()