import pandas as pd 
import sys
import re 
import time

def calculateMostColor(passed_df):
    most_frequent_color = passed_df['pixel_color'].mode()
    color_frequency = max(passed_df['pixel_color'].value_counts())
    
    return (most_frequent_color, color_frequency)

def calculateMostPixel(passed_df):
    most_frequent_coord = passed_df.groupby(['x', 'y']).size().reset_index(name='frequency').sort_values(by='frequency', ascending=False).iloc[0]
    return (most_frequent_coord.iloc[0], most_frequent_coord.iloc[1], most_frequent_coord.iloc[2])

# Read parquet file
pandasDf = pd.read_parquet('processed_canvas.parquet')

# Process timestamp column into datetime format
pandasDf['timestamp'] = pd.to_datetime(pandasDf['timestamp'])

# Define format of user input
YMD = r"^\d{4}-\d{2}-\d{2} \d{1,2} \d{4}-\d{2}-\d{2} \d{1,2}$"

# If incorrect format, let user know
if len(sys.argv) != 5:
    print("Required format: Start Date (YYYY-MM-DD H) End Date (YYYY-MM-DD H)")
# Parse user input and execute program
else:
    # Get user input
    user_input = ' '.join(sys.argv[1:5])
    # print("User input: ", user_input)

    if re.match(YMD, user_input) and sys.argv[2] < sys.argv[4]:
        startDate = ' '.join(sys.argv[1:2])
        startTime = ' '.join(sys.argv[2:3])
        endDate = ' '.join(sys.argv[3:4])
        endTime = ' '.join(sys.argv[4:5])

        startDateTime = pd.Timestamp(f"{startDate} {startTime}:00:00")
        endDateTime = pd.Timestamp(f"{endDate} {endTime}:00:00")
        print(f"Timeframe: {startDateTime} to {endDateTime}")

        # Start timing
        start_timer = time.perf_counter_ns()
        
        filtered_df = pandasDf[(pandasDf['timestamp'] >= startDateTime) & (pandasDf['timestamp'] <= endDateTime)]
        frequent_color, color_frequency = calculateMostColor(filtered_df)
        x_pixel, y_pixel, pixel_frequency = calculateMostPixel(filtered_df)

        # End timer
        end_timer = time.perf_counter_ns()

        # Calculate elapsed time
        elapsed_time_ns = end_timer - start_timer
        elapsed_time_ms = elapsed_time_ns / 1_000_000

        print(f"Elapsed time (ms): {elapsed_time_ms}")
        print(f"Most Popular Color: {frequent_color} ({color_frequency} occurences)")
        print(f"Most Popular Pixel: {x_pixel},{y_pixel} ({pixel_frequency} occurences)")
    else:
        print("Invalid format: Start Date (YYYY-MM-DD H) End Date (YYYY-MM-DD H)")
    