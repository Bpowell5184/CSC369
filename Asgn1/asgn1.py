import sys
import re


def analyzePlace(startDate, startTime, endDate, endTime):
    print("analyzing beep boop")

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
        print(f"Start date/time is {startDate} {startTime}, end date/time is {endDate} {endTime}")
        analyzePlace(startDate, startTime, endDate, endTime)
    else:
        print("Invalid format: Start Date (YYYY-MM-DD H) End Date (YYYY-MM-DD H)")

