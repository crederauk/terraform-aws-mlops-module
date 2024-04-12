import importlib
import pandas as pd
import argparse
import os


# Function to parse hyperparameters passed by SageMaker
def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--algorithm_choice", type=str)
    parser.add_argument("--target", type=str)

    return parser.parse_known_args()


def training_data(train_data_path, target, algorithm_choice):
    # Import Pycaret library depending on the algorithm choice
    pycaret = importlib.import_module(f"pycaret.{algorithm_choice}")

    # Load training data
    train_data = pd.read_csv(train_data_path)

    # Initialize data in PyCaret with all the defined parameters
    pycaret.setup(data=train_data, target=target, session_id=123)

    # Train and evaluate the performance of all estimators available in
    # the model library using cross-validation.
    best_model = pycaret.compare_models()

    # Save the trained model (this is an example, adjust based
    # on how you want to save your model)
    pycaret.save_model(best_model, "/opt/ml/model/best_model.pkl")


if __name__ == "__main__":
    args, _ = parse_args()

    training_data_path = os.path.join(
        "/opt/ml/input/data/training", "training_data.csv"
    )

    training_data(training_data_path, args.target, args.algorithm_choice)
