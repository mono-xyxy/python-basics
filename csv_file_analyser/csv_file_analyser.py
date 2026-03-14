import csv

print("csv file analyser")

file_name = input("Enter csv file name: ")

with open(file_name,"r",encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)

rows = len(data)-1
columns = len(data[0])

print("\nCSV Analysis")
print(f"Total Rows: {rows}")
print(f"Total Columns: {columns}")

print("\nColumn Names:")

for col in data[0]:
    print(col)
