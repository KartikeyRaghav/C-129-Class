import csv
import pandas as pd

dataset_1 = []
dataset_2 = []

with open('final.csv', r) as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)

with open('PSCompPars_2021.07.02_18.15.33.csv', r) as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_2.append(row)

header_1 = dataset_1
planet_data_1 = dataset_1[0:]
header_2 = dataset_2
planet_data_2 = dataset_2[0:]

final_header = header_1 + header_2
final_planet_data = []

for index, data in enumerate(planet_data_1):
    final_planet_data.append(planet_data_1[index]+planet_data_2[index])

with open('final.csv', a+) as f:
    csv_writer = csv.writer(f)
    csv_writer.write(headers)
    csv_writer.write(planet_data)