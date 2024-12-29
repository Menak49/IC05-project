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

def group_values(fichier) :
    if fichier.endswith('.xlsx'):  # Si le fichier est un Excel
        df = pd.read_excel(fichier)
    elif fichier.endswith('.csv'):  # Si le fichier est un CSV
        df = pd.read_csv(fichier)
    else:
        print(f"Erreur pour : {fichier}")


    modif=[]
    for i,row in df.iterrows():
        if ',' in str(row['event_subtype']):
            print(row)
            val=str(row['event_subtype']).split(',')

            print(val)
            for v in val:

                add=row.copy()
                add['event_subtype']=v.strip()

                modif.append(add)
        else:
            modif.append(row)
    df_modif= pd.DataFrame(modif)
    print(modif)

    df_modif.to_excel('Data2_V3.xlsx', index=False)
"""         
    if 'event_subtype' in df.columns:
        attack_type=df['event_subtype'].tolist()
        print("top")

    if 'incident_type' in df.columns:
        attack_type=df['incident_type'].tolist()


    attack_type=list(set(attack_type)) #suppression des doublons avec un passage en set

    group_attack = []
    for elt in attack_type:
        if type(elt)==str:
            group_attack.append([x.strip() for x in elt.split(',')])
        print(elt,"\n")

    longueur=len(df)

    df= pd.DataFrame(fichier, index=['year','actor_type','industry','event_type','event_subtype','country','actor_country','long','lat'])
    for i in range (1,longueur+1):
        value= df.loc[i,'event_subtype']
        for line in attack_type:
            if value == line:
"""

    #print (len(attack_type))
    #print(group_attack)



#change_value_quanti("Database2_nettoye.xlsx")
#change_value_quanti("Data2_V2_nettoye.xlsx")

group_values("Data2_v2_nettoye_nettoye.xlsx")