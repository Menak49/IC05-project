import pandas as pd

def modif_val(fichier):
    if fichier.endswith('.xlsx'):  #Si le fichier est un Excel
        df = pd.read_excel(fichier)
    elif fichier.endswith('.csv'):  #Si le fichier est un CSV
        df = pd.read_csv(fichier)
    else:
        print(f"Erreur pour : {fichier}")

    df.replace("Korea (the Democratic People's Republic of)", "North Korea")
    df.replace("Bonaire, Sint Eustatius and Saba", "Bonaire")
    df.replace("Taiwan (Province of China)", "Taïwan")
