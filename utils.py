#cleaning helper functions

# verify which columns are empy 95% and drop them
def clear_columns_with_95_percent_of_nan(df, columns_):
    """
    This function filters out the columns in a DataFrame that have more than 95% NaN values.
    Parameters:
    df (pandas.DataFrame): The DataFrame to filter.
    columns_ (list): The list of columns to consider for filtering.

    Returns:
    list: The list of filtered columns.
    """
    mask = (df[columns_].isnull().mean() <= 0.95)
    filtered_columns = df[columns_].columns[mask]
    return list(filtered_columns)

def clear_not_varying_cols_(df, columns):
    """
    This function removes the columns from a DataFrame that have only one unique value.

    Parameters:
    df (pandas.DataFrame): The DataFrame from which columns are to be removed.
    columns (list): The list of columns to consider for removal.

    Returns:
    pandas.DataFrame: The DataFrame after removing the columns with only one unique value.
    """
    for col in columns:
        if df[col].nunique() == 1:
            df = df.drop(col, axis=1)
    return list(df.columns)
