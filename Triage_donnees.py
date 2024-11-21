import csv
from geopy.geocoders import Nominatim

# suppression de certaines colonnes inutiles

attaques = []  # liste des différentes attaques
pays = {}

with open('Cyber Events Database - Records thru June 2024.csv', encoding=' ISO-8859-1', newline='') as file:
    with open('Triage_donnees.csv', 'w', encoding=' ISO-8859-1', newline='') as file_out:
        writer = csv.writer(file_out, delimiter=';')
        reader = csv.reader(file, delimiter=';')
        i = 0
        for row in reader:
            writer.writerow(row[1:6] + row[8:-2])
            if row[11] not in attaques:
                attaques.append(row[11])
            if row[-2] not in pays.values():
                pays[i] = row[-2]
                i += 1

# traitement pour les longitudes et latitudes
pays.pop(0)
pays[36] = "North Korea"  # petite correction d'un bug lié à la detection de la Corée du Nord
geolocator = Nominatim(user_agent='location')
lat_long = []
pays_loc = {}
for key in pays:
    location = geolocator.geocode(pays[key])
    if location:
        lat_long.append((location.latitude, location.longitude))
    else:
        lat_long.append((0, 0))
for key, val in pays.items():
    new_key = lat_long[key - 1]
    pays_loc[new_key] = val
