import pandas as pd


def preprocess_data(df):
    """This placeholder function is supposed to mock some dataframe pre-processing to b used in unit testing
    Args:
        df: input dataframe
    Returns:
    df: processed dataframe"""

    # One-hot-encode categorical columns
    df = pd.get_dummies(data=df, columns=["col1", "col2"])

    # Create some dummy columns
    df["col4"] = df["col3"] + 23
    df["col5"] = (df["col3"] + 100) / df["col4"]

    return df
