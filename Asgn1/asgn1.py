import sys
import re

def processLine(curLine):
    # Split line into list
    info = curLine.strip().split(',')
    # Get everything but coords (finnicky commas)
    columns = info[:3]
    date, time, loc = columns[0].strip().split(' ')
    color = columns[2]
    # Join rest together to form coordinate
    coordinate = ''.join(info[3:]).replace("\"", '').strip()
    # Return relevant info
    return date, time[0:2], color, coordinate


def analyzePlace(startDate, startTime, endDate, endTime):
    file_path = "../2022_place_canvas_history.csv"
    with open(file_path, "r") as file:
        # Skip the header
        next(file)
        # Create two dictionaries, color and coord respectively
        color_dict = {}
        coord_dict = {}
        # Process file line by line
        for line in file:
            # Process single line
            (curDate, curTime, color, coord) = processLine(line)

            # Check if the current line is past the end time
            if (curDate > endDate) or (curDate == endDate and curTime > endTime):
                break

            # Check if the current line is within the start time range
            if (curDate > startDate) or (curDate == startDate and curTime >= startTime):
                # Increment count for color
                if color in color_dict:
                    # Increment existing color
                    color_dict[color] += 1
                else:
                    # Add color
                    color_dict[color] = 1

                # Increment counts for coordinate
                if coord in coord_dict:
                    # Increment exisiting coordinate
                    coord_dict[coord] += 1
                else:
                    # Add coordinate
                    coord_dict[coord] = 1
    
    # Get most popular color and coordinate
    popular_color = max(color_dict.items(), key=lambda x: x[1], default=(None, 0))
    popular_coordinate = max(coord_dict.items(), key=lambda x: x[1], default=(None, 0))

    # Print results
    print(f"Most Popular Color: {popular_color[0]} ({popular_color[1]} occurrences)")
    print(f"Most Popular Coordinate: {popular_coordinate[0]} ({popular_coordinate[1]} occurrences)")

        

# Format: YYYY-MM-DD H
# Ex: 2004-09-27 12
YMD = r"^\d{4}-\d{2}-\d{2} \d{1,2} \d{4}-\d{2}-\d{2} \d{1,2}$"

if len(sys.argv) != 5:
    print("Required format: Start Date (YYYY-MM-DD H) End Date (YYYY-MM-DD H)")
else:
    # Get user input
    user_input = ' '.join(sys.argv[1:5])
    # print("User input: ", user_input)

    if re.match(YMD, user_input) and sys.argv[2] < sys.argv[4]:
        startDate = ' '.join(sys.argv[1:2])
        startTime = ' '.join(sys.argv[2:3])
        endDate = ' '.join(sys.argv[3:4])
        endTime = ' '.join(sys.argv[4:5])
        analyzePlace(startDate, startTime, endDate, endTime)
    else:
        print("Invalid format: Start Date (YYYY-MM-DD H) End Date (YYYY-MM-DD H)")

