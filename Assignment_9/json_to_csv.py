import csv
import json

csv_file = input("Enter CSV file name: ")
json_file = input("Enter JSON file name: ")

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

with open(json_file, "w") as file:
    json.dump(data, file, indent=4)

print("CSV file converted to JSON successfully.")


#'''
#Output:

#Enter CSV file name: sample.csv
#Enter JSON file name: sample.json
#CSV file converted to JSON successfully.
#'''