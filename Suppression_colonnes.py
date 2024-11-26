import pandas as pd

def nettoyer_fichier_excel(fichier_excel, colonnes_a_supprimer):
    # Modifier les options d'affichage
    pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
    pd.set_option('display.width', None)        # Ajuste la largeur pour éviter les coupures
    pd.set_option('display.max_colwidth', None) # Affiche tout le contenu des cellules

    # Trouver le nom du fichier sans extension
    nb = fichier_excel.find('.')

    # Charger le fichier Excel
    df = pd.read_excel(fichier_excel)

    print("Affichage avant nettoyage :")
    print(df.iloc[0:5])  # Affichage avant nettoyage

    # Supprimer les colonnes spécifiées
    df = df.drop(columns=colonnes_a_supprimer)

    print("\n\nFichier nettoyé de ses colonnes : \n")

    # Sauvegarder dans un nouveau fichier Excel
    nouveau_fichier = fichier_excel[:nb] + "_nettoye.xlsx"
    df.to_excel(nouveau_fichier, index=False)

    print("Affichage après nettoyage :")
    print(df.iloc[0:10])  # Affichage après nettoyage

    return df  # Retourner le DataFrame nettoyé


def ajouter_colonne(fichier_excel, list_colonnes):
    # Modifier les options d'affichage
    pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
    pd.set_option('display.width', None)        # Ajuste la largeur pour éviter les coupures
    pd.set_option('display.max_colwidth', None) # Affiche tout le contenu des cellules

    # Trouver le nom du fichier sans extension
    nb = fichier_excel.find('.')

    # Charger le fichier Excel
    df = pd.read_excel(fichier_excel)

    print("Affichage avant nettoyage :")
    print(df.iloc[0:5])  # Affichage avant nettoyage

    # Supprimer les colonnes spécifiées
    df = df.drop(columns=colonnes_a_supprimer)

    print("\n\nFichier nettoyé de ses colonnes : \n")

    # Sauvegarder dans un nouveau fichier Excel
    nouveau_fichier = fichier_excel[:nb] + "_nettoye.xlsx"
    df.to_excel(nouveau_fichier, index=False)

    print("Affichage après nettoyage :")
    print(df.iloc[0:10])  # Affichage après nettoyage

    return df  # Retourner le DataFrame nettoyé


import pandas as pd

def afficher_fichiers(fichiers_excel):
    # Modifier les options d'affichage
    pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
    pd.set_option('display.width', None)        # Ajuste la largeur pour éviter les coupures
    pd.set_option('display.max_colwidth', None) # Affiche tout le contenu des cellules

    # Traiter chaque fichier de la liste
    for fichier in fichiers_excel:
        # Vérifier l'extension et lire le fichier en fonction de son type
        if fichier.endswith('.xlsx'):  # Si le fichier est un Excel
            df = pd.read_excel(fichier)
        elif fichier.endswith('.csv'):  # Si le fichier est un CSV
            df = pd.read_csv(fichier)
        else:
            print(f"Erreur pour : {fichier}")
            continue  # Passer au fichier suivant si le type n'est ni Excel ni CSV

        # Affichage du fichier et des 10 premières lignes
        print(f"\nFichier : {fichier}")
        print(df.iloc[0:10])  # Affiche les 10 premières lignes du fichier





if "__main__" == __name__:
    # Exemple d'utilisation
    fichier_excel = "Data2_v2.xlsx"
    #colonnes_a_supprimer = ['slug', 'industry_code', 'change_log']  # Colonnes à supprimer
    #df_nettoye = nettoyer_fichier_excel(fichier_excel, colonnes_a_supprimer)
    print("ouin ouin ")
    # Liste des fichiers à traiter
    fichiers_excel = ["Data2.xlsx", "Data2_v2.xlsx"]  # Liste des fichiers à modifier selon les besoins
    # Appel de la fonction pour traiter les fichiers
    afficher_fichiers(fichiers_excel)
