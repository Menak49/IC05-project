



import pandas as pd

# Modifier les options d'affichage
pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
pd.set_option('display.width', None)       # Ajuste la largeur pour éviter les coupures
pd.set_option('display.max_colwidth', None)  # Affiche tout le contenu des cellules


fichier_excel = "Data1_v2.xlsx"
nb = fichier_excel.find('.')




df = pd.read_excel(fichier_excel)

print(df.iloc[0:5])  # Affichage avant


colonne_limite = 'cyber_conflict_issue'




colonne_a_renommer = input("\nColonne à renommer :")

new_name = input("Quelle est le nouveau nom?")

df = df.rename(columns={colonne_a_renommer: new_name})
# sauvegarder dans un nouveau fichier Excel
df.to_excel(fichier_excel[:nb] + "_v2" + ".xlsx", index=False)



print("\n\ncolonne renommée \n")



print(df.iloc[0:10])  # Affichage apres


