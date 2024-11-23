



import pandas as pd

# Modifier les options d'affichage
pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
pd.set_option('display.width', None)       # Ajuste la largeur pour éviter les coupures
pd.set_option('display.max_colwidth', None)  # Affiche tout le contenu des cellules


fichier_excel = "Data2.xlsx"



# Charger la première feuille du fichier Excel
df = pd.read_excel(fichier_excel)

print(df.iloc[0:5])  # Affichage avant

# Supprimer les colonnes (par nom)
colonnes_a_supprimer = ['month', 'industry_code', 'event_subtype', 'source_url']
df = df.drop(columns=colonnes_a_supprimer)


print("\n\nFichier nettoyé de ses colonnes : \n")

# Sauvegarder dans un nouveau fichier Excel
df.to_excel("Data2_v2.xlsx", index=False)

print(df.iloc[0:10])  # Affichage apres


