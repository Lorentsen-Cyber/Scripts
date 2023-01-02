import re, pyperclip


#FIXME:#text to search through, from clipboard
#text_to_search = pyperclip.paste()
text = '''
Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range
from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day
or month is a single digit, it’ll have a leading zero.
The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept
nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and
year, and write additional code that can detect if it is a valid date. April, June, September, and November
have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap
years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year
is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized
regular expression that can detect a valid date.
'''

#Regex for standard date format, returns a list of tuples
date_regex = re.compile(r'([0-3][0-9])/([0-1][0-9])/([1-2][0-9][0-9][0-9])')
#'dates' contain the results of the regex search 
dates = date_regex.findall(text)
#'31', '02', '2020' . '31', '04', '2021'
#print(dates)

#TODO: Loop through the list might need a 2D-list

for tuple in dates:
    if tuple[1] == '02' and int(tuple[0]) > 28:
        print('invalid date')

    if tuple[1] == 0:
        print(0)
