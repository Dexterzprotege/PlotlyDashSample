import pandas as pd

def data_frame():
    csv_file_path = "assets/tesla_vehicles.csv"
    df = pd.read_csv(csv_file_path)
    return df