from mlops_ml_models.transfom_data import split_data, preprocess_df
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
