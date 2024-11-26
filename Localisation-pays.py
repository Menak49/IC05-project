


import pandas as pd
from geopy.geocoders import Nominatim

def replace_list(cle,replacement, list):
    index = list.index(cle)
    list[index] = replacement

# Modifier les options d'affichage
pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
pd.set_option('display.width', None)       # Ajuste la largeur pour éviter les coupures
pd.set_option('display.max_colwidth', None)  # Affiche tout le contenu des cellules

fichiers_excel = ["Data2.xlsx", "Data2_v2.xlsx"]# Liste des fichiers à traiter à modifier selon les besoins


for fichier in fichiers_excel:
    if fichier.endswith('.xlsx'):  #Si le fichier est un Excel
        df = pd.read_excel(fichier)
    elif fichier.endswith('.csv'):  #Si le fichier est un CSV
        df = pd.read_csv(fichier)
    else:
        print(f"Erreur pour : {fichier}")



pays = df["country"].unique().tolist()



index_undetermined1 = pays.index("Undetermined")
pays.pop(index_undetermined1)
replace_list("Korea (the Democratic People's Republic of)", "North Korea",pays)
replace_list("Bonaire, Sint Eustatius and Saba", "Bonaire",pays)
replace_list("Taiwan (Province of China)", "Taïwan",pays)



noms_attaquants = df["actor_country"].unique().tolist()


index_undetermined2 = noms_attaquants.index("Undetermined")
noms_attaquants.pop(index_undetermined2)
replace_list("Korea (the Democratic People's Republic of)", "North Korea",noms_attaquants)


pays_tot = pays
for country in noms_attaquants:
    if country not in pays_tot:
        pays_tot.append(country)


geolocator = Nominatim(user_agent='location')
dico_local_pays = {}
for i in range(0, len(pays_tot)):

    location = geolocator.geocode(pays[i])
    if location:
        dico_local_pays[pays_tot[i]] = [location.latitude, location.longitude]
    else:
        print(pays_tot[i])




print(pays_tot)
print("lallalala " , len(pays_tot))

print(dico_local_pays)
print(len(dico_local_pays))

print(pays)
print("lallalala " , len(pays))
print(noms_attaquants)
print("lallalala " , len(noms_attaquants))
print(f"\nFichier : {fichier}")

print(df.iloc[0:10])











