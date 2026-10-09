import os
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

from src.data_loader import get_project_root, import_data
from src.preprocessing import create_reduced_dataset
from src.train import train

def evaluate_model():

    X_train, X_test, y_train, y_test = import_data()
    X_test_reduced = create_reduced_dataset(X_test)

    print("Loading the Final Pipeline")
    final_pipeline_path = os.path.join(get_project_root(), "models", "final_pipeline_model")
    final_pipeline = joblib.load(final_pipeline_path)
    print("Final Pipeline loaded")

    y_test_preds = final_pipeline.predict(X_test_reduced)
    accuracy = accuracy_score(y_test, y_test_preds)

    # Initialize the Confusion Matrix\
    plt.figure(figsize=(8, 6))
    labels = ['KIRC', 'BRCA', 'PRAD', 'LUAD', 'COAD']
    cm = confusion_matrix(y_test, y_test_preds,
                          labels=labels)
    disp = ConfusionMatrixDisplay(cm, display_labels=labels)
    disp.plot()

    plt.title('Test Confusion Matrix')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')

    # Save the Confusion Matrix
    project_root = get_project_root()
    cm_path = os.path.join(project_root, "reports", "figures", "confusion_matrix")
    plt.savefig(cm_path)
    print(f"Confusion Matrix saved at: {cm_path}")

    print(f"Test set accuracy score: {accuracy}")

if __name__ == "__main__":
    evaluate_model()