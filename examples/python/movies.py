import csv
import json
import datetime

csvfile = open('tmdb_5000_movies.csv', 'r')
jsonfile = open('movies.json', 'w')

# fieldnames = ("FirstName","LastName","IDNumber","Message")
fieldnames = ( "budget","genres","homepage","id","keywords","original_language","original_title","overview","popularity","production_companies","production_countries","release_date","revenue","runtime","spoken_languages","status","tagline","title","vote_average","vote_count")

reader = csv.DictReader( csvfile, fieldnames)
for row in reader:

    json.dump(row, jsonfile)
    jsonfile.write('\n')

# print(datetime.datetime.now().timestamp())

# with open('tmdb_5000_movies.csv', 'r') as inf, open('file.json', 'wb') as outf:
#     csvreader = csv.DictReader(inf)
#     fieldnames = ['Timestamp'] + csvreader.fieldnames  # add column name to beginning
#     csvwriter = csv.DictWriter(outf, fieldnames)
#     csvwriter.writeheader()
#     for node in enumerate(csvreader):
#         csvwriter.writerow(dict(row, Timestamp=datetime.datetime.now().timestamp().toString()))