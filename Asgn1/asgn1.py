import sys
import re
# Get time from command line

# Format: YYYY-MM-DD H
# Ex: 2004-09-27 12
YMD = r"^\d{4}-\d{2}-\d{2} \d{1,2} \d{4}-\d{2}-\d{2} \d{1,2}$"

if len(sys.argv) != 5:
    print("Required format: Start Date (YYYY-MM-DD H) End Date (YYYY-MM-DD H)")
else:
    # Get user input
    user_input = ' '.join(sys.argv[1:5])
    # print("User input: ", user_input)

    if re.match(YMD, user_input):
        startDate = ' '.join(sys.argv[1:3])
        endDate = ' '.join(sys.argv[3:5])
        # print(f"Start date is {startDate}, end date is {endDate}")
    else:
        print("Invalid format: Start Date (YYYY-MM-DD H) End Date (YYYY-MM-DD H)")


def analyzePlace(startTime, endTime):
    print("analyzing beep boop")