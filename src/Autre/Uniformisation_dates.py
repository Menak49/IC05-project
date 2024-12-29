
import pandas as pd

# Modifier les options d'affichage
pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
pd.set_option('display.width', None)       # Ajuste la largeur pour éviter les coupures
pd.set_option('display.max_colwidth', None)  # Affiche tout le contenu des cellules

fichier = "cyber_attack.csv"
nb = fichier.find('.')

dico_mois = {
    'janvier': 1,
    'février': 2,
    'mars': 3,
    'avril': 4,
    'mai': 5,
    'juin': 6,
    'juillet': 7,
    'août': 8,
    'septembre': 9,
    'octobre': 10,
    'novembre': 11,
    'décembre': 12
}

df = pd.read_csv(fichier)

# Remplacer toutes les valeurs de la colonne 'nom_colonne' par une nouvelle valeur
df['nom_colonne'] = df['date'].apply(lambda x:
                                     f"{x.split()[2]}-{dico_mois[x.split()[1].lower()]:02d}-{int(x.split()[0]):02d}")

# Sauvegarder le DataFrame modifié dans un nouveau fichier CSV
df.to_csv(fichier[:nb] + "_v2" + ".csv", index=False)

# Afficher le DataFrame modifié
print(df)











