import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pycaret.classification import setup as setup_classification, create_model as create_model_classification, get_config as get_config_classification
from pycaret.regression import setup as setup_regression, create_model as create_model_regression, get_config as get_config_regression


def split_data(df: pd.DataFrame, shuffle: bool) -> pd.DataFrame:
    """This script split the data into test_data and train_data,
    with optional shuffle function

    Note:
        Remember that this function returns 2 values, therefore using,
        make sure you declare 2 variables using this function
        ex.(train_data, test_data = split_data(df, shuffle=True))

    Args:
        df (pd.DataFrame): dataframe that you want to split
        shuffle (boolean): If true, function will shuffle the dataframe,
        else the order of data will remain the same

    Returns:
        pd.DataFrame: train_data
        pf.DataFrame: test_data
    """
    try:
        if shuffle:
            df = df.sample(frac=1).reset_index(drop=True)

        train_size = int(0.8 * len(df))
        train_data = df[:train_size]
        test_data = df[train_size:]

        return train_data, test_data
    except Exception as e:
        print(f"Error loading data: {e}")


def preprocess_df(df, preprocessing_script_path):
    """This is a placeholder function to import the preprocess_data function
    if it has been uploaded into s3 when the preprocessing_script_path is provided by the user.
    Args:
    df:
    preprocessing_script_path: Path to the data preprocessing script declared in user's repo

    Returns:
        df: dataframe that has been processed or unchanged depending
        if the preprocessing_script_path has been provided
    """
    if preprocessing_script_path:
        try:
            print("Loading file")
            from preprocess_data import preprocess_data

            df = preprocess_data(df)
            assert isinstance(df, pd.DataFrame)
        except ImportError:
            print("File does not exist")
    return df


def feature_selection(data, target_variable, algorithm_choice, threshold=None):
    """This function takes in a dataframe and performs feature importance analysis on the features within the data, using
    either the ridge classifier or linear regressor based on the type of analysis, and then returns a modified dataframe of
    the original data but only with the important features kept.

    Args:
        data (pd.DataFrame): dataframe that you want to perform feature selection on
        target_variable (str): Name of the column that is the target feature
        algorithm_choice (str): Name of the algorithm being used, must be either 'classification' or 'regression'
        threshold (float): A number between 0-1 to manually set the threshold above which features are kept. If no
                           value is passed, it defaults to the max feature importance minus 1 standard deviation.

    Returns:
        pd.DataFrame: data_important_features
    """

    if algorithm_choice == "classification":
        s = setup_classification(data=data, target=target_variable, fold=3, session_id=123)
        model = create_model_classification("ridge")
        coefficients = np.abs(model.coef_).mean(axis=0)
        X_train_transformed = get_config_classification('X_train')

    elif algorithm_choice == "regression":
        s = setup_regression(data=data, target=target_variable, session_id=123)
        model = create_model_regression("lr")
        coefficients = model.coef_
        X_train_transformed = get_config_regression('X_train')

    else:
        print(f"The algorithm {algorithm_choice} is not supported for feature selection, only classification and regression analysis is supported.")
        return pd.DataFrame([])



    feature_importance = pd.Series(coefficients, index=X_train_transformed.columns).sort_values(ascending=False).to_frame()
    feature_importance.rename(columns={0: 'importance'}, inplace=True)

    if threshold is None:
        std = feature_importance['importance'].std()
        max_importance = feature_importance['importance'].max()
        threshold = max_importance - std

    print('\n\nFeature importance dataframe:')
    print(feature_importance)
    print('\n')

    important_features = feature_importance[feature_importance['importance'] > threshold].index.tolist()
    discarded_features = feature_importance[feature_importance['importance'] <= threshold].index.tolist()

    # Plot feature importances
    plt.bar(important_features, feature_importance.loc[important_features, 'importance'], color='darkblue', label='Kept Features')
    plt.bar(discarded_features, feature_importance.loc[discarded_features, 'importance'], color='grey', label='Discarded Features')
    plt.xlabel('Features')
    plt.ylabel('Importance')
    plt.title('Feature Importances')
    plt.axhline(y=threshold, color='r', linestyle='--', label=f'Threshold = {threshold:.2f}')
    plt.xticks(rotation=90)
    plt.legend()
    plt.show()

    print(f"Keeping features: {important_features}\n")
    print(f"Discarding features: {discarded_features}\n")

    data_important_features = data[important_features + [target_variable]]

    return data_important_features
