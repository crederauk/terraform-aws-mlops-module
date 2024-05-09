import pandas as pd
import numpy as np
from pycaret.classification import setup, get_config
from sklearn.linear_model import RidgeClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import matplotlib.pyplot as plt


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


def one_hot_encode(data):
    categorical_columns = data.select_dtypes(include=['object']).columns.tolist()

    encoder = OneHotEncoder(sparse_output=False)

    one_hot_encoded = encoder.fit_transform(data[categorical_columns])

    one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(categorical_columns))

    df_encoded = pd.concat([data, one_hot_df], axis=1)

    df_encoded = df_encoded.drop(categorical_columns, axis=1)

    return df_encoded, categorical_columns


def normalise_data(data):
    # Data normalisation
    numeric_features = data.drop(columns=[target_variable]).select_dtypes(include=np.number).columns.tolist()

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(data[numeric_features])

    scaled_data = pd.DataFrame(scaled_features, columns=numeric_features)
    scaled_data = pd.concat([scaled_data, data[data.columns.difference(numeric_features)]], axis=1)

    df_encoded, categorical_columns = one_hot_encode(scaled_data)

    return df_encoded, categorical_columns


def feature_selection(data, target_variable):
    processed_data, categorical_columns = normalise_data(data)

    # Setup Ridge classifier
    s = setup(data=processed_data, target=target_variable, feature_selection=False)

    X_train = get_config('X_train')
    y_train = get_config('y_train')

    print("Getting feature importances...")
    print("Creating Ridge model...")
    model = RidgeClassifier()
    model.fit(X_train, y_train)

    # Extract feature importance dataframe
    feature_importance = pd.DataFrame(np.abs(model.coef_[0]),
                                      index=X_train.columns,
                                      columns=['importance']).sort_values('importance', ascending=False)

    # reverse the one hot encoding by averaging the importance for the encoded columns
    for col in categorical_columns:
        unique = data[col].unique()
        tot_importance = 0
        for s in unique:
            col_name = f"{col}_{s}"
            col_importance = feature_importance['importance'][col_name]
            print(f"{col_name}: {col_importance}")
            tot_importance += col_importance
            feature_importance = feature_importance.drop(index=col_name)
        avg_importance = tot_importance / len(unique)
        feature_importance.loc[col] = avg_importance

    feature_importance = feature_importance.sort_values(by='importance', ascending=False)
    print('\n\nFeature importances:')
    print(feature_importance)
    print('\n')

    std = feature_importance['importance'].std()
    max_importance = feature_importance['importance'].max()
    threshold = max_importance - std

    important_features = feature_importance[feature_importance['importance'] > threshold].index.tolist()
    discarded_features = feature_importance[feature_importance['importance'] <= threshold].index.tolist()

    print(f"Keeping features: {important_features}\n")
    print(f"Discarding features: {discarded_features}\n")

    # Plot feature importances
    plt.bar(important_features, feature_importance.loc[important_features, 'importance'], color='darkblue',
            label='Kept Features')
    plt.bar(discarded_features, feature_importance.loc[discarded_features, 'importance'], color='grey',
            label='Discarded Features')
    plt.xlabel('Features')
    plt.ylabel('Importance')
    plt.title('Feature Importances from Ridge Classifier')
    plt.xticks(rotation=90)
    plt.legend()
    plt.show()

    # Return modifed dataframe
    data_important_features = data[important_features + [target_variable]]
    return data_important_features
