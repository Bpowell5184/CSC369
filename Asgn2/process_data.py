import pandas as pd

chunk_size = 10000
chunks = pd.read_csv('../2022_place_canvas_history.csv', header=0, usecols=[0, 2, 3], nrows=20000, skip_blank_lines=True, parse_dates=[0], chunksize=chunk_size)

chunk_list = []

for chunk in chunks:
    chunk_list.append(chunk)

processed_df = pd.concat(chunk_list, ignore_index=True)

processed_df['timestamp'] = processed_df['timestamp'].str.replace(' UTC', '', regex=False)

processed_df['timestamp'] = pd.to_datetime(processed_df['timestamp'], errors='coerce')

processed_df.to_parquet('processed_canvas.parquet', engine='auto', compression='snappy')

new_df = pd.read_parquet('processed_canvas.parquet')
print(new_df.head())