import polars as pl
import time
from datetime import datetime

# hardcode start/end dates/times
start_date = "2022-04-01"
start_hour = "13"
end_date = "2022-04-01"
end_hour = "14"

# Convert to valid format
startDateTime = datetime.strptime(f"{start_date} {start_hour}:00:00", "%Y-%m-%d %H:%M:%S")
endDateTime = datetime.strptime(f"{end_date} {end_hour}:00:00", "%Y-%m-%d %H:%M:%S")

# Print timeframe
print(f"Timeframe: {startDateTime} to {endDateTime}")

# Start time
start_timer = time.perf_counter_ns()

# Read to Polars df
df = pl.read_parquet('processed_canvas.parquet')

# Get dates between start and end datetime
filtered_df = df.filter(
    (pl.col("timestamp") >= startDateTime) & (pl.col("timestamp") <= endDateTime)
)

# Find most frequent color
most_frequent_color = (
    filtered_df
    .group_by('pixel_color')
    .agg(pl.len().alias("frequency"))
    .sort("frequency", descending=True)
    .limit(1)
)

# Find most frequent pixel coord
most_frequent_pixel = (
    filtered_df
    .group_by(['x', 'y'])
    .agg(pl.len().alias("frequency"))
    .sort("frequency", descending=True)
    .limit(1)
)

# End timer
end_timer = time.perf_counter_ns()

# Calculate elapsed time
elapsed_time_ns = end_timer - start_timer
elapsed_time_ms = elapsed_time_ns / 1_000_000

print(f"Elapsed time (ms): {elapsed_time_ms}")
print(f"Most Popular Color: {most_frequent_color['pixel_color']} ({most_frequent_color['frequency']} occurences)")
print(f"Most Popular Pixel: {most_frequent_pixel['x']},{most_frequent_pixel['y']} ({most_frequent_pixel['frequency']} occurences)")