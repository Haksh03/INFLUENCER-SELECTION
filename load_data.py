# load_data.py

import pandas as pd

def load_data(excel_path):
    """
    Load data from the provided Excel file path.
    """
    try:
        df = pd.read_excel(excel_path)
        return df
    except Exception as e:
        print(f"Error loading data from {excel_path}: {e}")
        return None
