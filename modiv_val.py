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



def change_value_quanti(fichier):
    if fichier.endswith('.xlsx'):  # Si le fichier est un Excel
        df = pd.read_excel(fichier)
    elif fichier.endswith('.csv'):  # Si le fichier est un CSV
        df = pd.read_csv(fichier)
    else:
        print(f"Erreur pour : {fichier}")

    df=df.fillna(0)
    df=df.replace('Undetermined',0)
    df=df.replace(' - ',0)
    df=df.replace('Not available',0)

    if  'start_date' in df.columns:
        df['start_date']=df['start_date'].replace(0,pd.NaT)
        df['start_date']=pd.to_datetime(df['start_date'])
        df['start_date']=df['start_date'].dt.year
        df = df.fillna(0)

    nb = fichier.find('.')
    nouveau_fichier = fichier[:nb] + "_nettoye.xlsx"
    df.to_excel(nouveau_fichier, index=False)
    return df


change_value_quanti("Database2_nettoye.xlsx")
change_value_quanti("Data2_V2_nettoye.xlsx")