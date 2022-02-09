import csv
import sys
import os
import time
import re

file_location = "/Users/connorhanwick/Desktop/SFAB - IT Support/Tickets/Ticketing Interface.csv"
keywords = ["printer", "mac", "apple", "lenovo", "windows","chrome","lexmark","outlook"]
tickets_count = 0

def parse_files(file, keyword):
    index = 1

    with open(file, 'r') as f:
        reader = csv.reader(f)

        for r in reader:
            line = r[1]
            check = re.search(keyword, line, re.IGNORECASE)
            if check != None:
                global tickets_count
                tickets_count += 1
                print(line)

            
def stat_puller(list):
    """Takes a list of keywords and returns if/how frequently each occurs in a csv"""


    for keyword in list:
        print(f' - - - -{keyword.upper()} {tickets_count} - - - - ')
        parse_files(file_location, keyword)



if __name__ == "__main__":
    # parse_files(file_location, "printer")
    stat_puller(keywords)