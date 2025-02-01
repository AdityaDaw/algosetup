# Check if last row's Pct_Change is greater than 5
import pandas as pd
from pandas import DataFrame



def check_change_is_greater(df: DataFrame,number :float = 3):
    last_pct_change = df['change'].iloc[-1]  # Get last row's percentage change
    is_greater_than = last_pct_change > number if pd.notna(last_pct_change) else False  # Handle NaN
    return is_greater_than
