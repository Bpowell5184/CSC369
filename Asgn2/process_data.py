import pandas as pd
import re

def is_valid_date(date_str):
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(?: UTC)?$'
    return bool(re.match(pattern, date_str))

chunk_size = 10000
chunks = pd.read_csv('../2022_place_canvas_history.csv', header=0, usecols=[0, 2, 3], skip_blank_lines=True, chunksize=chunk_size)

chunk_list = []

for chunk in chunks:
    if 'timestamp' in chunk.columns:
        chunk = chunk[chunk['timestamp'].apply(is_valid_date)]

    chunk['timestamp'] = pd.to_datetime(
        chunk['timestamp'].str.replace(' UTC', '', regex=False),
        format='%Y-%m-%d %H:%M:%S',
        errors='coerce'
    )

    chunk_list.append(chunk)

# Combine chunks
processed_df = pd.concat(chunk_list, ignore_index=True)

# Process file with x and y columns, dropping old coordinates column
processed_df[['x', 'y']] = processed_df['coordinate'].str.split(',', expand=True)
processed_df.drop(['coordinate'], axis=1, inplace=True)

# Sort values by timestamp
processed_df = processed_df.sort_values(by=['timestamp'])

# Convert to parquet for better storage
print(processed_df.head())
processed_df.to_parquet('processed_canvas.parquet', engine='auto', compression='snappy')