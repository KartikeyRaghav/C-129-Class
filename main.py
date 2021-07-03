import csv

data = []

with open('PSCompPars_2021.07.02_18.15.33.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)

headers = data[0]
planet_data = data[1:]

# Converting the planet name to the lower case
for dataset in planet_data:
    dataset[1] = dataset[1].lower()

planet_data.sort(key=lambda, planet_data:planet_data[1])

with open('PSCompPars_2021.07.02_18.15.33.csv', 'a+') as f:
    csv_writer = csv.writer(f)
    csv_writer.write(headers)
    csv_writer.write(planet_data)