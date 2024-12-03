# calculate_performance.py

def calculate_performance(df):
    """
    Calculate average performance for each Face_Group.
    """
    grouped_data = df.groupby('Face_Group').agg({
        'Performance': ['mean', 'std', 'count']
    }).reset_index()
    grouped_data.columns = ['Face_Group', 'Avg_Performance', 'Performance_Std', 'Video_Count']
    return grouped_data
