from mlops_ml_models.transform_data import split_data, preprocess_df, feature_selection
import pandas as pd
import pytest


@pytest.fixture
def mock_df() -> pd.DataFrame:
    """This creates a mock dataframe based on the data
    entered in the columns below. The data in the mock
    dataframe is the same data that we have in the csv file in the
    resources section The aim of this is to be able to test if the
    load_data.py file returns a the same dataframe as what we have here.

    Returns:
        pd.DataFrame: dataframe created from the script. Should be the same as
        in the resources.
    """
    return pd.DataFrame(
        {
            "col1": [1, 2, 3, 1, 2, 3, 1, 2, 3, 1],
            "col2": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A"],
            "col3": [4.5, 5.5, 6.5, 4.5, 5.5, 6.5, 4.5, 5.5, 6.5, 6.5],
        }
    )

def mock_df_2() -> pd.DataFrame:
    """This creates a mock dataframe based on the data
    entered in the columns below. col1 is the 'feature', cols 2-5 are directly
    related to col1 and so should have strong feature importance, cols 6-9 are
    not related to col1 and so should have low feature importance

    Returns:
        pd.DataFrame: dataframe created from the script. Should be the same as
        in the resources.
    """
    return pd.DataFrame(
        {
            "col1": [1, 2, 3, 1, 2, 3, 1, 2, 3, 1],
            "col2": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A"],
            "col3": [2, 3, 4, 2, 3, 4, 2, 3, 4, 2],
            "col4": [1, 4, 9, 1, 4, 9, 1, 4, 9, 1],
            "col5": [1, 1.41, 1.73, 1, 1.41, 1.73, 1, 1.41, 1.73, 1],
            "col6": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "col7": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            "col8": [0.08, 0.21, 0.63, 0.32, 0.81, 0.73, 0.92, 0.39, 0.66, 0.51],
            "col9": ["G", "W", "M", "Q", "S", "P", "G", "Z", "C", "A"],
            "col1_again": [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
        }
    )


def test_split_data_shuffle(mock_df: pd.DataFrame) -> None:
    """This Test compares if the split_data correctly splits a dataframe into 80% and 20% of rows with shuffling.

    Args:
        mock_df (pd.DataFrame): Mock data generated from mock_df function
    """
    train_data, test_data = split_data(mock_df, shuffle=True)
    assert len(train_data) == 8 and len(test_data) == 2


def test_split_data(mock_df: pd.DataFrame) -> None:
    """This Test compares if the split_data correctly splits a dataframe into 80% and 20% of rows with no shuffling.

    Args:
        mock_df (pd.DataFrame): Mock data generated from mock_df function
    """
    train_data, test_data = split_data(mock_df, shuffle=False)
    assert list(train_data["col1"]) == [1, 2, 3, 1, 2, 3, 1, 2] and list(
        test_data["col1"]
    ) == [3, 1]


def test_preprocess_df(mock_df: pd.DataFrame) -> None:
    """This test checks if the pre-processing function can be imported and execute a custom script to update the dataframe.

    Args:
    mock_df: mock dataframe"""
    preprocessing_script_path = "tests\\preprocess_data.py"
    df = preprocess_df(mock_df, preprocessing_script_path)

    assert len(df.columns) == 9


def test_preprocess_df_no_path(mock_df: pd.DataFrame) -> None:
    """This test checks if the pre-processing function doesn't change the data if the preprocessing_script_path is not present.

    Args:
    mock_df: mock dataframe"""
    preprocessing_script_path = None
    df = preprocess_df(mock_df, preprocessing_script_path)

    assert df.equals(mock_df)

def test_feature_selection(mock_df_2: pd.DataFrame) -> None:
    """This test checks if the feature selection function is able to only select the important features in the mock_df_2 dataframe.

    Args:
    mock_df_2: mock dataframe"""

    df = feature_selection(mock_df_2)

    non_important_cols = ['col6', 'col7', 'col8', 'col9']

    assert not df.index.isin(non_important_cols).any()