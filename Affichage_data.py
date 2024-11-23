



import pandas as pd

# Modifier les options d'affichage
pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
pd.set_option('display.width', None)       # Ajuste la largeur pour éviter les coupures
pd.set_option('display.max_colwidth', None)  # Affiche tout le contenu des cellules


fichier_excel = "Data2.xlsx" # Modifier le nom pour changer de fichier



df = pd.read_excel(fichier_excel)




# Afficher les premières lignes
print(df.iloc[0:10])




