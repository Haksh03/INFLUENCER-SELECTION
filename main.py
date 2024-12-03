# main.py

from load_data import load_data
from process_videos import process_videos
from calculate_performance import calculate_performance

def main():
    # Load data
    excel_path = "C:/Users/haksh/Downloads/Assignment Data.xlsx"
    df = load_data(excel_path)
    if df is None:
        return

    # Process videos
    df = process_videos(df)

    # Save processed video data
    processed_path = "ProcessedVideos_videos.xlsx"
    df.to_excel(processed_path, index=False)
    print(f"Processed data saved to {processed_path}")

    # Calculate and save performance metrics
    performance_metrics = calculate_performance(df)
    metrics_path = "PerformanceMetrics_videos.xlsx"
    performance_metrics.to_excel(metrics_path, index=False)
    print(f"Performance metrics saved to {metrics_path}")

if __name__ == "__main__":
    main()
