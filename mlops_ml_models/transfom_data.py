import pandas as pd


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


# TODO finish
def preprocess_df(df, preprocessing_script_path):
    """"""
    if preprocessing_script_path:
        try:
            print("Loading file")
            from preprocess_data import preprocess_data

            df = preprocess_data(df)
            message = "preprocess_data function didn't return a dataframe"
            assertIsInstance(df, pd.DataFrame, message)
        except ImportError:
            print("File does not exist")
    return df
