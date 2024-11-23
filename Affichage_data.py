
import pandas as pd

# Modifier les options d'affichage
pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
pd.set_option('display.width', None)       # Ajuste la largeur pour éviter les coupures
pd.set_option('display.max_colwidth', None)  # Affiche tout le contenu des cellules

fichiers_excel = ["Data2.xlsx", "Data1.xlsx", "cyber_attack.csv"]# Liste des fichiers à traiter à modifier selon les besoins


for fichier in fichiers_excel:
    if fichier.endswith('.xlsx'):  #Si le fichier est un Excel
        df = pd.read_excel(fichier)
    elif fichier.endswith('.csv'):  #Si le fichier est un CSV
        df = pd.read_csv(fichier)
    else:
        print(f"Erreur pour : {fichier}")


    print(f"\nFichier : {fichier}")
    print(df.iloc[0:10])











