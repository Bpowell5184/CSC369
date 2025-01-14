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
        # Process current line
        curLine = file.readline()
        (curDate, curTime, color, coord) = processLine(curLine)
        # If line is past end time, end read
        
        # Change color and coord counts
        

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

