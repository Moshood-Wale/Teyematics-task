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
body_rows = file_opening(path)[1:]
print(header_row)
