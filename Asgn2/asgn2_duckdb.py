import duckdb
import time

# hardcode start/end dates/times
start_date = "2022-04-02"
start_hour = "04"
end_date = "2022-04-02"
end_hour = "10"

# Convert to valid format
startDateTime = f"{start_date} {start_hour}:00:00"
endDateTime = f"{end_date} {end_hour}:00:00"

# Print timeframe
print(f"Timeframe: {startDateTime} to {endDateTime}")

# Connect to duckdb
dbConnect = duckdb.connect()

# Start time
start_timer = time.perf_counter_ns()

# Query data that only is in bounds of start/end time
filtered_query = f"""
SELECT * 
FROM read_parquet('processed_canvas.parquet')
WHERE timestamp >= TIMESTAMP '{startDateTime}' AND timestamp <= TIMESTAMP '{endDateTime}'
"""

# Query for max color
color_query = f"""
SELECT pixel_color, COUNT(*) AS frequency
FROM ({filtered_query}) AS filtered_data
GROUP BY pixel_color
ORDER BY frequency DESC
LIMIT 1
"""

# Query for max coord
pixel_query = f"""
SELECT x, y, COUNT(*) AS frequency
FROM ({filtered_query}) AS filtered_data
GROUP BY x, y
ORDER BY frequency DESC
LIMIT 1
"""

# Turn to vars
most_frequent_color = dbConnect.execute(color_query).fetchone()
most_frequent_pixel = dbConnect.execute(pixel_query).fetchone()

# Get results
color, color_frequency = most_frequent_color
x_pixel, y_pixel, pixel_frequency = most_frequent_pixel

# End timer
end_timer = time.perf_counter_ns()

# Calculate elapsed time
elapsed_time_ns = end_timer - start_timer
elapsed_time_ms = elapsed_time_ns / 1_000_000

print(f"Elapsed time (ms): {elapsed_time_ms}")
print(f"Most Popular Color: {most_frequent_color} ({color_frequency} occurences)")
print(f"Most Popular Pixel: {x_pixel},{y_pixel} ({pixel_frequency} occurences)")