import re

    
def file_opening(filename):

    try:
        file_extension = re.split('\.', filename)  
        if file_extension[1] == 'csv' :
            with open(filename) as file:
                return file.readlines()
        else:
            return None
    except FileNotFoundError:
        return None
path = "posts.csv"
header_row = file_opening(path)[0]
header_array = header_row[1:].lstrip().split()
body_rows = file_opening(path)[1:]

# def extract_header():

#     try:
#         listed_lines = file_opening()
#         header = f"{listed_lines[0]}"
#         create_schema = 
#     except:
#         return("This file is not supported or found")

