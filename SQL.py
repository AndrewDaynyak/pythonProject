import csv
file_path='C:/Users/Lenovo/Desktop/survey.csv'

with open(file_path, 'r') as file:
    reader=csv.reader(file)
    next(reader)
    for row  in reader:
        print(row[1])