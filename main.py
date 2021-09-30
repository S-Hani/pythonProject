import requests
import json
import csv

prtcl = "http"
url = "www.omdbapi.com"
params = {
    "apikey": "926c06e4",
    "s": "Avengers"
}
payload = {}
headers = {}


def dict_to_query(parameters, domain, protocol):
    query = ''
    for key in parameters.keys():
        query += str(key) + '=' + str(parameters[key]) + "&"
    return protocol + "://" + domain + "/?" + query


response = requests.request("GET", dict_to_query(params, url, prtcl), headers=headers, data=payload)
data = json.loads(response.text)
search_data = data['Search']

# Path to the CSV file
csv_file_path = 'movies.csv'
csv_file = open(csv_file_path, 'w')
# create the csv writer object
csv_writer = csv.writer(csv_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for attributes in search_data:
    if count == 0:
        # Writing headers of CSV file
        header = attributes.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(attributes.values())
csv_file.close()

csv_file = open(csv_file_path, 'r')
reader = csv.reader(csv_file)
for row in reader:
    print(" ".join(row))
csv_file.close()
