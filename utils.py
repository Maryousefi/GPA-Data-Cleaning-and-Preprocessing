import pandas as pd

def drop_unnecessary_columns(df):
    """
    Drops columns that contain 'Unnamed' in their header,
    typically from CSV index artifacts.
    """
    return df.drop(columns=[col for col in df.columns if 'Unnamed' in col], errors='ignore')

def clean_missing_ids(df, id_column):
    """
    Removes rows where the specified ID column has missing values.
    """
    return df[df[id_column].notna()]

def clean_and_validate_gpa(df):
    """
    Retains rows with GPA values between 0 and 4.0 inclusive.
    """
    return df[df['GPA'].between(0, 4.0)]
